"""
Control de velocidad de requests para scraping ético y sostenible.
Implementa delays aleatorios con distribución que simula comportamiento humano.
Incluye simulación de fatiga: los delays crecen conforme avanza la sesión.
"""

import random
import time
from dataclasses import dataclass, field

from utils.logger import setup_logger

logger = setup_logger("rate_limiter")


@dataclass
class RateLimiter:
    """
    Controlador de velocidad con delays aleatorios y fatiga progresiva.

    Usa distribución triangular para simular patrones humanos
    (la mayoría de pausas cerca de la media, con colas ocasionales).

    La fatiga simula que un usuario real va más lento conforme pasa
    el tiempo navegando: tras 30 min los delays suben ~20%, tras 1h ~40%.
    """

    min_delay: float = 2.0
    max_delay: float = 5.0
    delay_entre_municipios: float = 5.0  # Delay base entre comunidades
    burst_delay: float = 8.0  # Delay largo ocasional para romper patrones
    burst_probability: float = 0.08  # 8% de probabilidad de pausa larga
    _request_count: int = 0
    _session_start: float = field(default_factory=time.time)
    _municipios_count: int = 0

    def _fatigue_factor(self) -> float:
        """
        Calcula el factor de fatiga según el tiempo transcurrido.
        Un humano real navega más lento conforme pasa el tiempo.

        Returns:
            Multiplicador >= 1.0 (sin fatiga al inicio).
        """
        elapsed_min = (time.time() - self._session_start) / 60
        if elapsed_min < 15:
            return 1.0
        elif elapsed_min < 30:
            return 1.1  # +10%
        elif elapsed_min < 60:
            return 1.25  # +25%
        else:
            return 1.4  # +40%

    def wait(self) -> float:
        """
        Espera un tiempo aleatorio antes del próximo request.
        Ocasionalmente introduce pausas más largas para simular
        comportamiento humano irregular. Los delays crecen con la fatiga.

        Returns:
            Tiempo de espera efectivo en segundos.
        """
        self._request_count += 1
        fatigue = self._fatigue_factor()

        # Cada ~10 requests, pausa larga para romper patrones
        if random.random() < self.burst_probability:
            delay = random.uniform(self.burst_delay, self.burst_delay * 2)
            delay *= fatigue
            logger.debug(
                f"Pausa larga (anti-patrón): {delay:.1f}s "
                f"[request #{self._request_count}, fatiga x{fatigue:.2f}]"
            )
        else:
            # Distribución triangular: moda en el punto medio
            mode = (self.min_delay + self.max_delay) / 2
            delay = random.triangular(self.min_delay, self.max_delay, mode)
            delay *= fatigue
            logger.debug(
                f"Delay estándar: {delay:.1f}s [request #{self._request_count}]"
            )

        time.sleep(delay)
        return delay

    def wait_between_municipios(self) -> float:
        """
        Espera más larga entre cambios de comunidad.
        Simula un usuario que busca una comunidad, descansa,
        y luego busca la siguiente. Se alarga con la fatiga.

        Returns:
            Tiempo de espera efectivo en segundos.
        """
        self._municipios_count += 1
        fatigue = self._fatigue_factor()
        delay = random.uniform(self.delay_entre_municipios, self.delay_entre_municipios * 2)
        delay *= fatigue
        logger.info(
            f"Pausa entre comunidades: {delay:.1f}s "
            f"[comunidad #{self._municipios_count}]"
        )
        time.sleep(delay)
        return delay

    def wait_between_sessions(self) -> float:
        """
        Pausa larga entre sesiones de navegador (rotación de sesión).
        Simula un usuario que cierra el navegador, hace otra cosa,
        y vuelve más tarde.

        Returns:
            Tiempo de espera efectivo en segundos.
        """
        delay = random.uniform(45, 90)  # 45s-1.5min
        logger.info(
            f"Pausa entre sesiones: {delay:.0f}s "
            f"({delay/60:.1f} min)"
        )
        time.sleep(delay)
        return delay

    def reset_session(self) -> None:
        """Reinicia el reloj de fatiga (nueva sesión de navegador)."""
        self._session_start = time.time()
        logger.debug("Reloj de fatiga reiniciado")

    @property
    def total_requests(self) -> int:
        """Número total de requests realizados."""
        return self._request_count

    @property
    def session_minutes(self) -> float:
        """Minutos transcurridos en la sesión actual."""
        return (time.time() - self._session_start) / 60
