// Motor D3 agnóstico para el hub "Canarias en Datos".
//
// Port directo del prototipo vivienda_storytelling_d3_divi.html, extrayendo
// todo lo específico de Vivienda a una configuración de temática declarativa.
// El motor reutiliza D3 v7 cargado desde CDN al primer uso.

import { SUPABASE_CONFIG, GEO_FALLBACK } from "./config.js";

const D3_CDN = "https://cdn.jsdelivr.net/npm/d3@7";

let d3Promise = null;
function loadD3() {
  if (window.d3) return Promise.resolve(window.d3);
  if (d3Promise) return d3Promise;
  d3Promise = new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = D3_CDN;
    script.async = true;
    script.onload = () => resolve(window.d3);
    script.onerror = () => reject(new Error("No se pudo cargar D3 desde CDN"));
    document.head.appendChild(script);
  });
  return d3Promise;
}

const monthNames = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];

const ccaaNameMap = {
  "Andalucia": "Andalucía",
  "Andalucía": "Andalucía",
  "Aragon": "Aragón",
  "Aragón": "Aragón",
  "Asturias": "Principado de Asturias",
  "Principado de Asturias": "Principado de Asturias",
  "Balears, Illes": "Islas Baleares",
  "Baleares": "Islas Baleares",
  "Illes Balears": "Islas Baleares",
  "Islas Baleares": "Islas Baleares",
  "Canarias": "Canarias",
  "Cantabria": "Cantabria",
  "Castilla y Leon": "Castilla y León",
  "Castilla y León": "Castilla y León",
  "Castilla-La Mancha": "Castilla-La Mancha",
  "Castilla La Mancha": "Castilla-La Mancha",
  "Cataluna": "Cataluña",
  "Cataluña": "Cataluña",
  "Catalunya": "Cataluña",
  "Comunitat Valenciana": "Comunidad Valenciana",
  "Comunidad Valenciana": "Comunidad Valenciana",
  "Extremadura": "Extremadura",
  "Galicia": "Galicia",
  "Madrid": "Comunidad de Madrid",
  "Comunidad de Madrid": "Comunidad de Madrid",
  "Murcia": "Región de Murcia",
  "Region de Murcia": "Región de Murcia",
  "Región de Murcia": "Región de Murcia",
  "Navarra": "Comunidad Foral de Navarra",
  "Comunidad Foral de Navarra": "Comunidad Foral de Navarra",
  "Pais Vasco": "País Vasco",
  "País Vasco": "País Vasco",
  "La Rioja": "La Rioja",
  "Rioja, La": "La Rioja",
  "Ceuta": "Ceuta",
  "Ciudad de Ceuta": "Ceuta",
  "Melilla": "Melilla",
  "Ciudad de Melilla": "Melilla",
};

const mapPalette = ["#f3f8fb", "#dcecf3", "#bddbe9", "#89bed8", "#4b98c5", "#1769aa"];

function stripAccents(value) {
  return String(value || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function ccaaKey(value) {
  return stripAccents(value).toLowerCase().replace(/^\d{1,2}\s+/, "").replace(/[^a-z0-9]+/g, " ").trim();
}

const ccaaKeyMap = new Map(Object.entries(ccaaNameMap).map(([raw, canonical]) => [ccaaKey(raw), canonical]));

function normalizeCcaaName(value) {
  if (!value) return "";
  const direct = ccaaNameMap[value];
  if (direct) return direct;
  return ccaaKeyMap.get(ccaaKey(value)) || String(value).trim();
}

function normalizeGender(value) {
  const key = stripAccents(value).toLowerCase().trim();
  if (["hombre", "hombres", "male", "m"].includes(key)) return "hombre";
  if (["mujer", "mujeres", "female", "f"].includes(key)) return "mujer";
  return key || "";
}

function compactCcaaLabel(name) {
  const labels = {
    "Principado de Asturias": "Asturias",
    "Islas Baleares": "Baleares",
    "Castilla y León": "CyL",
    "Castilla-La Mancha": "CLM",
    "Comunidad Valenciana": "C. Valenciana",
    "Comunidad de Madrid": "Madrid",
    "Comunidad Foral de Navarra": "Navarra",
    "Región de Murcia": "Murcia",
    "País Vasco": "P. Vasco",
  };
  return labels[name] || name;
}

function parseNumber(value) {
  if (value === undefined || value === null || value === "" || value === "NA") return null;
  const text = String(value).trim();
  const parsed = Number(text.includes(",") ? text.replace(/\./g, "").replace(",", ".") : text);
  return Number.isFinite(parsed) ? parsed : null;
}

function parsePeriod(row) {
  const raw = row.periodo ?? row.anio ?? row.year ?? row.fecha ?? row.mes;
  const label = row.periodo_label || row.periodoLabel || row.fecha || row.mes || raw;
  const rawText = String(label ?? raw ?? "").trim();
  const isoMonth = rawText.match(/^(\d{4})[-/](\d{1,2})(?:[-/]\d{1,2})?(?:[T\s].*)?$/);
  const spanishDate = rawText.match(/^(\d{1,2})[-/](\d{1,2})[-/](\d{4})$/);
  const compactMonth = rawText.match(/^(\d{4})(\d{2})$/);
  let year = null;
  let month = null;

  if (isoMonth) {
    year = +isoMonth[1];
    month = +isoMonth[2];
  } else if (spanishDate) {
    year = +spanishDate[3];
    month = +spanishDate[2];
  } else if (compactMonth) {
    year = +compactMonth[1];
    month = +compactMonth[2];
  } else if (/^\d{4}$/.test(String(raw ?? "").trim())) {
    year = +raw;
  } else {
    const matchedYear = rawText.match(/\d{4}/);
    year = matchedYear ? +matchedYear[0] : +raw;
    const monthWords = {
      ene: 1, enero: 1, feb: 2, febrero: 2, mar: 3, marzo: 3,
      abr: 4, abril: 4, may: 5, mayo: 5, jun: 6, junio: 6,
      jul: 7, julio: 7, ago: 8, agosto: 8, sep: 9, sept: 9, septiembre: 9, setiembre: 9,
      oct: 10, octubre: 10, nov: 11, noviembre: 11, dic: 12, diciembre: 12,
    };
    const normalized = stripAccents(rawText).toLowerCase();
    const matchedMonth = Object.keys(monthWords).find(name => new RegExp(`\\b${name}\\b`).test(normalized));
    if (matchedMonth) month = monthWords[matchedMonth];
  }

  if (!Number.isFinite(year)) year = null;
  if (!Number.isFinite(month) || month < 1 || month > 12) month = null;
  const value = year === null ? null : month ? year + ((month - 1) / 12) : year;
  const key = year === null ? rawText : month ? `${year}-${String(month).padStart(2, "0")}` : String(year);
  const display = year === null ? rawText : month ? `${monthNames[month - 1]} ${year}` : String(year);
  return { key, value, label: display, year, month };
}

function displayPeriodLabel(raw) {
  if (!raw && raw !== 0) return "";
  const text = String(raw).trim();
  const parsed = parsePeriod({ periodo: text, periodo_label: text });
  return parsed.label || text;
}

function shellHtml(topic, { includeGender, availableScenes }) {
  const sceneNav = availableScenes
    .map((scene, i) => `
      <button class="ced-story-step${i === 0 ? " is-active" : ""}" data-ced-step="${scene.id}" type="button">
        <strong>${i + 1}. ${escapeHtml(scene.title)}</strong>
        <span>${escapeHtml(scene.sub || "")}</span>
      </button>`)
    .join("");

  const modeOptions = availableScenes
    .map(scene => `<option value="${scene.id}">${escapeHtml(scene.title)}</option>`)
    .join("");

  const methodItems = (topic.method || [])
    .map(item => `<div class="ced-method-item"><h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(item.body)}</p></div>`)
    .join("");

  const tablesNote = includeGender
    ? `Tablas: \`${topic.data.globalTable}\` y \`${topic.data.genderTable}\``
    : `Tabla: \`${topic.data.globalTable}\``;

  return `
    <section class="ced-header">
      <div class="ced-header-inner">
        <div>
          <div class="ced-eyebrow">${escapeHtml(topic.eyebrow)}</div>
          <h2>${escapeHtml(topic.title)}</h2>
          <div class="ced-lead">${escapeHtml(topic.lead)}</div>
        </div>
        <div class="ced-actions">
          <button class="ced-btn" type="button" data-ced-method>Metodología</button>
          <button class="ced-btn is-primary" type="button" data-ced-download>Descargar CSV</button>
        </div>
      </div>
      <div class="ced-toolbar">
        <div class="ced-control"><label>Indicador</label><select data-ced-metric></select></div>
        <div class="ced-control"><label>Periodo</label><select data-ced-year></select></div>
        <div class="ced-control"><label>Lectura</label><select data-ced-mode>${modeOptions}</select></div>
      </div>
    </section>
    <div class="ced-main">
      <nav class="ced-story-nav" aria-label="Capítulos narrativos">${sceneNav}</nav>
      <section class="ced-stage">
        <div class="ced-kpi-row" data-ced-kpis></div>
        <section class="ced-panel">
          <div class="ced-panel-head">
            <div>
              <div class="ced-panel-title" data-ced-title>${escapeHtml(availableScenes[0]?.title || "")}</div>
              <div class="ced-panel-sub" data-ced-sub>Cargando datos...</div>
            </div>
            <div class="ced-badge" data-ced-badge>Datos del workflow</div>
          </div>
          <div class="ced-chart-wrap" data-ced-chart><div class="ced-loading">Cargando datos...</div></div>
          <div class="ced-method-grid" data-ced-method-grid hidden>${methodItems}</div>
          <div class="ced-source-strip">
            <span data-ced-source>${escapeHtml(topic.sourceText || "")}</span>
            <span>${escapeHtml(tablesNote)}</span>
          </div>
        </section>
      </section>
    </div>
    <div class="ced-tooltip" data-ced-tooltip></div>
  `;
}

function escapeHtml(str) {
  return String(str ?? "").replace(/[&<>"']/g, ch => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[ch]));
}

export async function renderTopic(rootEl, topic) {
  const d3 = await loadD3();
  rootEl.innerHTML = "";
  rootEl.classList.add("ced-topic-root");

  const includeGender = Boolean(topic.data?.genderTable);
  const availableScenes = (topic.scenes || []).filter(s => s.type !== "gender" || includeGender);
  if (!availableScenes.length) throw new Error(`La temática "${topic.id}" no declara escenas.`);

  // Construir metricMeta (indexable por key) a partir de topic.metrics
  const metricMeta = {};
  for (const m of topic.metrics) {
    metricMeta[m.key] = {
      label: m.label,
      short: m.short || m.label,
      unit: m.unit || "",
      format: d3.format(m.format || ",.2f"),
      suffix: m.suffix || "",
      source: m.source || "",
      displayFactor: m.displayFactor || 1,
      hasGender: m.hasGender !== false,
      min: m.min,
      max: m.max,
    };
  }

  rootEl.innerHTML = shellHtml(topic, { includeGender, availableScenes });

  const q = selector => rootEl.querySelector(selector);
  const qa = selector => Array.from(rootEl.querySelectorAll(selector));
  const els = {
    metric: q("[data-ced-metric]"),
    year: q("[data-ced-year]"),
    mode: q("[data-ced-mode]"),
    chart: q("[data-ced-chart]"),
    title: q("[data-ced-title]"),
    sub: q("[data-ced-sub]"),
    badge: q("[data-ced-badge]"),
    kpis: q("[data-ced-kpis]"),
    methodGrid: q("[data-ced-method-grid]"),
    sourceText: q("[data-ced-source]"),
    tooltip: q("[data-ced-tooltip]"),
  };

  const state = {
    mode: availableScenes[0].id,
    metric: topic.defaultMetric || topic.metrics[0]?.key,
    year: null,
    periodKey: null,
    global: [],
    gender: [],
    geojson: null,
    sourceMode: "supabase",
  };

  // Dispatcher mode -> scene.type (por si en el futuro algún topic reutiliza un tipo con id distinto)
  const modeToType = new Map(availableScenes.map(s => [s.id, s.type]));
  const sceneById = new Map(availableScenes.map(s => [s.id, s]));

  function parseRow(row) {
    const period = parsePeriod(row);
    const out = {
      ccaa: normalizeCcaaName(row.ccaa || row.comunidad || row.NUTS_NAME || row.NAME_LATN),
      periodo: period.value,
      periodo_key: period.key,
      periodo_label: period.label,
      periodo_year: period.year,
      periodo_month: period.month,
      origen: row.origen || "real",
    };
    for (const key of Object.keys(metricMeta)) {
      out[key] = clampMetricValue(key, parseNumber(row[key]));
      out[`${key}_origen`] = row[`${key}_origen`] || row[`${key}_origin`] || row.origen || "real";
      out[`${key}_periodo_label`] = row[`${key}_periodo_label`] || row[`${key}_periodo`] || row.periodo_label || row.periodoLabel || period.label;
    }
    return out;
  }

  function parseGender(row) {
    const period = parsePeriod(row);
    const out = {
      ccaa: normalizeCcaaName(row.ccaa || row.comunidad || row.NUTS_NAME || row.NAME_LATN),
      periodo: period.value,
      periodo_key: period.key,
      periodo_label: period.label,
      periodo_year: period.year,
      periodo_month: period.month,
      genero: normalizeGender(row.genero),
      origen: row.origen || "real",
    };
    for (const key of Object.keys(metricMeta)) {
      out[key] = clampMetricValue(key, parseNumber(row[key]));
      out[`${key}_origen`] = row[`${key}_origen`] || row[`${key}_origin`] || row.origen || "real";
      out[`${key}_periodo_label`] = row[`${key}_periodo_label`] || row[`${key}_periodo`] || row.periodo_label || row.periodoLabel || period.label;
    }
    return out;
  }

  function coalesceRows(rows, keys) {
    const byKey = new Map();
    rows.forEach(row => {
      const id = keys.map(key => row[key]).join("||");
      if (!byKey.has(id)) {
        const base = {};
        keys.forEach(key => base[key] = row[key]);
        base.periodo = row.periodo;
        base.periodo_key = row.periodo_key;
        base.periodo_label = row.periodo_label;
        base.periodo_year = row.periodo_year;
        base.periodo_month = row.periodo_month;
        base.origen = row.origen || "real";
        Object.keys(metricMeta).forEach(metric => {
          base[metric] = null;
          base[`${metric}_origen`] = null;
          base[`${metric}_periodo_label`] = null;
        });
        byKey.set(id, base);
      }
      const target = byKey.get(id);
      if (row.origen === "real") target.origen = "real";
      Object.keys(metricMeta).forEach(metric => {
        if (row[metric] !== null && row[metric] !== undefined) {
          const incomingOrigin = row[`${metric}_origen`] || row.origen || "real";
          const currentOrigin = target[`${metric}_origen`];
          const shouldReplace = target[metric] === null || target[metric] === undefined || (currentOrigin !== "real" && incomingOrigin === "real");
          if (shouldReplace) {
            target[metric] = row[metric];
            target[`${metric}_origen`] = incomingOrigin;
            target[`${metric}_periodo_label`] = row[`${metric}_periodo_label`] || row.periodo_label;
          }
        }
      });
    });
    return Array.from(byKey.values()).sort((a, b) => d3.ascending(a.ccaa, b.ccaa) || d3.ascending(a.periodo, b.periodo));
  }

  function valueLabel(metric, value) {
    if (value === null || value === undefined || Number.isNaN(value)) return "s/d";
    const meta = metricMeta[metric];
    return `${meta.format(displayValue(metric, value))}${meta.suffix}`;
  }

  function displayValue(metric, value) {
    if (value === null || value === undefined || Number.isNaN(value)) return value;
    return value * (metricMeta[metric]?.displayFactor || 1);
  }

  function clampMetricValue(metric, value) {
    if (value === null || value === undefined || Number.isNaN(value)) return value;
    const meta = metricMeta[metric];
    let out = value;
    if (Number.isFinite(meta?.min)) out = Math.max(meta.min, out);
    if (Number.isFinite(meta?.max)) out = Math.min(meta.max, out);
    return out;
  }

  function deltaLabel(metric, value) {
    if (value === null || value === undefined || Number.isNaN(value)) return "s/d";
    const shown = displayValue(metric, value);
    const meta = metricMeta[metric];
    return `${shown > 0 ? "+" : ""}${meta.format(shown)}${meta.suffix}`;
  }

  function tooltipMetricLabel(metric = state.metric) {
    const meta = metricMeta[metric];
    const year = state.year || state.periodKey || "";
    return meta ? `${meta.label} (${String(year).slice(0, 4)})` : String(year).slice(0, 4);
  }

  function tooltipValue(text) { return `<span class="ced-tooltip-value">${text}</span>`; }

  function paddedExtent(values, padRatio = 0.08) {
    const extent = d3.extent(values.filter(Number.isFinite));
    if (extent[0] === undefined || extent[1] === undefined) return [0, 1];
    const range = extent[1] - extent[0];
    if (range === 0) {
      const pad = Math.max(Math.abs(extent[0]) * padRatio, 1);
      return [extent[0] - pad, extent[1] + pad];
    }
    return [extent[0] - range * padRatio, extent[1] + range * padRatio];
  }

  function availableMetrics() {
    return Object.keys(metricMeta).filter(metric => state.global.some(d => d[metric] !== null));
  }
  function availableGenderMetrics() {
    return Object.keys(metricMeta).filter(metric => metricMeta[metric].hasGender && state.gender.some(d => d[metric] !== null));
  }
  function metricsForMode(mode = state.mode) {
    return modeToType.get(mode) === "gender" ? availableGenderMetrics() : availableMetrics();
  }
  function metricRows(metric = state.metric) {
    const rows = modeToType.get(state.mode) === "gender" ? state.gender : state.global;
    return rows.filter(d => d[metric] !== null && d[metric] !== undefined && d.periodo_key);
  }
  function selectedMetricOrigin(row, metric = state.metric) {
    return row?.[`${metric}_origen`] || row?.origen || "real";
  }
  function rowPeriodLabel(row, metric = state.metric) {
    const raw = row?.[`${metric}_periodo_label`] || row?.periodo_label;
    if (raw && String(raw).trim()) return displayPeriodLabel(raw);
    if (row?.periodo_month) return `${monthNames[row.periodo_month - 1]} ${row.periodo_year}`;
    return row?.periodo_year ? String(row.periodo_year) : String(row?.periodo ?? "");
  }
  function currentPeriodLabel(metric = state.metric) {
    const rows = metricRows(metric).filter(d => d.periodo_key === state.periodKey);
    return rowPeriodLabel(rows[0], metric) || String(state.year ?? "");
  }
  function periodOptions(metric = state.metric) {
    const byKey = new Map();
    metricRows(metric).forEach(row => {
      if (!byKey.has(row.periodo_key)) {
        byKey.set(row.periodo_key, { key: row.periodo_key, value: row.periodo, label: rowPeriodLabel(row, metric), origins: new Set() });
      }
      byKey.get(row.periodo_key).origins.add(selectedMetricOrigin(row, metric));
    });
    return Array.from(byKey.values()).sort((a, b) => d3.ascending(a.value, b.value));
  }

  function refreshMetricOptions() {
    const allowed = metricsForMode();
    if (!allowed.includes(state.metric)) state.metric = allowed.includes(topic.defaultMetric) ? topic.defaultMetric : allowed[0];
    els.metric.innerHTML = "";
    for (const metric of allowed) {
      const option = document.createElement("option");
      option.value = metric;
      option.textContent = metricMeta[metric].label;
      els.metric.appendChild(option);
    }
    els.metric.value = state.metric;
  }

  function refreshPeriodOptions() {
    const periods = periodOptions();
    const previousKey = state.periodKey;
    if (!periods.length) {
      state.periodKey = null;
      state.year = null;
      els.year.innerHTML = "";
      return;
    }
    const selected = periods.find(d => d.key === previousKey) || periods[periods.length - 1];
    state.periodKey = selected.key;
    state.year = selected.value;
    els.year.innerHTML = "";
    for (const period of periods) {
      const option = document.createElement("option");
      const isProjection = period.origins.size > 0 && !period.origins.has("real");
      option.value = period.key;
      option.textContent = isProjection ? `${period.label} (proyección)` : period.label;
      els.year.appendChild(option);
    }
    els.year.value = state.periodKey;
  }

  function validRows(metric, periodKey = state.periodKey) {
    return state.global.filter(d => d.periodo_key === periodKey && d[metric] !== null);
  }
  function canariasRow(periodKey = state.periodKey) {
    return state.global.find(d => d.ccaa === "Canarias" && d.periodo_key === periodKey);
  }
  function previousCanariasRow(metric) {
    const current = canariasRow();
    if (!current) return null;
    const rows = state.global.filter(d => d.ccaa === "Canarias" && d[metric] !== null && d.periodo < current.periodo);
    if (!rows.length) return null;
    const exactKey = current.periodo_month ? `${current.periodo_year - 1}-${String(current.periodo_month).padStart(2, "0")}` : String(current.periodo_year - 1);
    return rows.find(d => d.periodo_key === exactKey) || d3.greatest(rows, d => d.periodo);
  }
  function median(rows, metric) { return d3.median(rows, d => d[metric]); }
  function rankCanarias(rows, metric) {
    const sorted = rows.slice().sort((a, b) => d3.descending(a[metric], b[metric]));
    return sorted.findIndex(d => d.ccaa === "Canarias") + 1;
  }

  function setMode(mode) {
    if (!sceneById.has(mode)) mode = availableScenes[0].id;
    state.mode = mode;
    els.mode.value = mode;
    qa("[data-ced-step]").forEach(btn => btn.classList.toggle("is-active", btn.dataset.cedStep === mode));
    refreshMetricOptions();
    refreshPeriodOptions();
    render();
  }

  function setupControls() {
    els.metric.innerHTML = "";
    els.year.innerHTML = "";
    refreshMetricOptions();
    refreshPeriodOptions();

    els.metric.addEventListener("change", event => { state.metric = event.target.value; refreshPeriodOptions(); render(); });
    els.year.addEventListener("change", event => {
      state.periodKey = event.target.value;
      const selected = periodOptions().find(d => d.key === state.periodKey);
      state.year = selected ? selected.value : state.year;
      render();
    });
    els.mode.addEventListener("change", event => setMode(event.target.value));
    qa("[data-ced-step]").forEach(btn => btn.addEventListener("click", () => setMode(btn.dataset.cedStep)));
    const methodBtn = q("[data-ced-method]");
    const methodScene = availableScenes.find(s => s.type === "method");
    if (methodBtn) {
      if (methodScene) methodBtn.addEventListener("click", () => setMode(methodScene.id));
      else methodBtn.style.display = "none";
    }
    q("[data-ced-download]").addEventListener("click", downloadFilteredCsv);
  }

  function renderKpis() {
    const type = modeToType.get(state.mode);
    if (type === "evolution") return renderEvolutionInsights();
    if (type === "gender") return renderGenderInsights();
    if (type === "method") return renderMethodInsights();
    return renderTerritoryInsights();
  }

  function setInsightCards(items) {
    els.kpis.innerHTML = items.map(([label, valueText, note]) => `
      <div class="ced-kpi"><div class="ced-kpi-label">${label}</div><div class="ced-kpi-value">${valueText}</div><div class="ced-kpi-note">${note}</div></div>
    `).join("");
  }

  function renderTerritoryInsights() {
    const rows = validRows(state.metric);
    const can = canariasRow();
    const value = can ? can[state.metric] : null;
    const prev = previousCanariasRow(state.metric);
    const delta = prev && prev[state.metric] !== null && value !== null ? value - prev[state.metric] : null;
    const med = median(rows, state.metric);
    const rank = rankCanarias(rows, state.metric);
    setInsightCards([
      ["Canarias", valueLabel(state.metric, value), currentPeriodLabel()],
      ["Cambio interanual", deltaLabel(state.metric, delta), prev ? `Frente a ${rowPeriodLabel(prev)}` : "Sin periodo comparable"],
      ["Mediana CCAA", valueLabel(state.metric, med), "Comunidades con dato"],
      ["Posición", rank ? `${rank}/${rows.length}` : "s/d", "Ordenado de mayor a menor"],
    ]);
  }

  function renderEvolutionInsights() {
    const byCcaa = Array.from(d3.group(state.global.filter(d => d[state.metric] !== null), d => d.ccaa), ([ccaa, values]) => {
      const sorted = values.sort((a, b) => d3.ascending(a.periodo, b.periodo));
      const first = sorted[0];
      const last = sorted[sorted.length - 1];
      return { ccaa, first, last, change: last[state.metric] - first[state.metric], years: `${rowPeriodLabel(first)}-${rowPeriodLabel(last)}` };
    }).filter(d => d.first && d.last);
    const can = byCcaa.find(d => d.ccaa === "Canarias");
    const maxGrowth = d3.greatest(byCcaa, d => d.change);
    const minGrowth = d3.least(byCcaa, d => d.change);
    const latestRows = validRows(state.metric, state.periodKey);
    const latestMedian = median(latestRows, state.metric);
    setInsightCards([
      ["Canarias", can ? deltaLabel(state.metric, can.change) : "s/d", can ? `Cambio ${can.years}` : "Serie sin dato"],
      ["Mayor aumento", maxGrowth ? maxGrowth.ccaa : "s/d", maxGrowth ? deltaLabel(state.metric, maxGrowth.change) : ""],
      ["Mayor descenso", minGrowth ? minGrowth.ccaa : "s/d", minGrowth ? deltaLabel(state.metric, minGrowth.change) : ""],
      ["Mediana último periodo", valueLabel(state.metric, latestMedian), currentPeriodLabel()],
    ]);
  }

  function renderGenderInsights() {
    const metric = state.metric;
    const rows = genderGapRows(metric);
    const can = rows.find(d => d.ccaa === "Canarias");
    const maxGap = d3.greatest(rows, d => Math.abs(d.gap));
    const positive = rows.filter(d => d.gap > 0).length;
    const avgGap = d3.mean(rows, d => d.gap);
    setInsightCards([
      ["Canarias", can ? deltaLabel(metric, can.gap) : "s/d", "Brecha mujeres - hombres"],
      ["Brecha más alta", maxGap ? maxGap.ccaa : "s/d", maxGap ? deltaLabel(metric, maxGap.gap) : ""],
      ["CCAA con brecha +", `${positive}/${rows.length}`, "Mayor valor en mujeres"],
      ["Brecha media", deltaLabel(metric, avgGap), currentPeriodLabel(metric)],
    ]);
  }

  function renderMethodInsights() {
    const ccaaCount = new Set(state.global.map(d => d.ccaa)).size;
    const sortedPeriods = Array.from(d3.group(state.global, d => d.periodo_key), ([, rows]) => rows[0]).sort((a, b) => d3.ascending(a.periodo, b.periodo));
    const periodExtent = sortedPeriods.length ? `${rowPeriodLabel(sortedPeriods[0])}-${rowPeriodLabel(sortedPeriods[sortedPeriods.length - 1])}` : "s/d";
    const projectedRows = state.global.filter(d => d.origen === "proyeccion").length;
    setInsightCards([
      ["Fuente activa", sourceBadge(), "Prioridad: Supabase > fallback geo"],
      ["Cobertura", `${ccaaCount} CCAA`, periodExtent],
      ["Filas globales", d3.format(",")(state.global.length), "Tras consolidar CCAA/año"],
      ["Proyecciones", d3.format(",")(projectedRows), "Filas con origen = proyeccion"],
    ]);
  }

  function genderGapRows(metric) {
    return Array.from(d3.group(state.gender.filter(d => d.periodo_key === state.periodKey && d[metric] !== null), d => d.ccaa), ([ccaa, values]) => {
      const men = values.find(d => d.genero === "hombre");
      const women = values.find(d => d.genero === "mujer");
      return men && women ? { ccaa, gap: women[metric] - men[metric], men: men[metric], women: women[metric] } : null;
    }).filter(Boolean);
  }

  function render() {
    renderKpis();
    els.chart.innerHTML = "";
    els.methodGrid.hidden = true;
    els.chart.style.display = "block";
    const rows = metricRows().filter(d => d.periodo_key === state.periodKey);
    const projected = rows.length > 0 && rows.every(d => selectedMetricOrigin(d) === "proyeccion");
    els.badge.textContent = projected ? "Incluye proyección" : sourceBadge();
    const type = modeToType.get(state.mode);
    if (type === "map") renderContext();
    else if (type === "evolution") renderEvolution();
    else if (type === "gender") renderGender();
    else if (type === "method") renderMethod();
  }

  function sourceBadge() {
    if (state.sourceMode === "supabase") return "Supabase";
    return "Datos locales";
  }

  function isCompactLayout() {
    return rootEl.getBoundingClientRect().width <= 640 || window.matchMedia("(max-width: 640px)").matches;
  }

  function chartSize() {
    const rect = els.chart.getBoundingClientRect();
    const compact = isCompactLayout();
    const type = modeToType.get(state.mode);
    const minHeight = compact
      ? ({ map: 430, evolution: 430, gender: 660, method: 360 }[type] || 430)
      : 460;
    return { width: Math.max(compact ? 300 : 320, rect.width), height: Math.max(minHeight, rect.height || minHeight) };
  }

  function renderContext() {
    const meta = metricMeta[state.metric];
    const sceneMeta = sceneById.get(state.mode);
    els.title.textContent = `${meta.label}: mapa autonómico`;
    els.sub.textContent = sceneMeta?.sub || `Mapa coroplético por comunidades autónomas en ${currentPeriodLabel()}.`;
    if (!state.geojson) return renderContextFallback();

    const rows = validRows(state.metric);
    const values = new Map(rows.map(d => [normalizeCcaaName(d.ccaa), d[state.metric]]));
    const { width, height } = chartSize();
    const compact = isCompactLayout();
    const margin = compact ? { top: 8, right: 8, bottom: 72, left: 8 } : { top: 14, right: 20, bottom: 58, left: 20 };
    const svg = d3.select(els.chart).append("svg").attr("viewBox", [0, 0, width, height]);
    const mainlandFeatures = state.geojson.features.filter(d => geoName(d) !== "Canarias");
    const canFeature = state.geojson.features.find(d => geoName(d) === "Canarias");
    const mainland = { type: "FeatureCollection", features: mainlandFeatures };
    const projection = d3.geoMercator().fitExtent([[margin.left, margin.top], [width - margin.right, height - margin.bottom]], mainland);
    const path = d3.geoPath(projection);
    const mapValues = rows.map(d => d[state.metric]).filter(Number.isFinite);
    const extent = d3.extent(mapValues);
    const uniqueValues = Array.from(new Set(mapValues)).sort(d3.ascending);
    const color = uniqueValues.length > 1
      ? d3.scaleQuantile().domain(mapValues).range(mapPalette)
      : () => mapPalette[Math.floor(mapPalette.length / 2)];

    function fillFor(name) {
      const value = values.get(normalizeCcaaName(name));
      if (value === undefined) return "#edf2f6";
      return color(value);
    }

    const mainlandPaths = svg.append("g").selectAll("path").data(mainlandFeatures).join("path")
      .attr("class", "ced-map-region")
      .attr("data-ced-region", d => normalizeCcaaName(geoName(d)))
      .attr("d", path)
      .attr("fill", d => fillFor(geoName(d)))
      .attr("stroke", "#ffffff")
      .attr("stroke-width", 0.8)
      .attr("cursor", "pointer")
      .on("pointermove", function(event, d) {
        d3.select(this).raise().attr("stroke", "#17212b").attr("stroke-width", 2.2);
        const name = geoName(d);
        showTooltip(event, name, tooltipValue(valueLabel(state.metric, values.get(normalizeCcaaName(name)))));
      })
      .on("pointerleave", function() { d3.select(this).attr("stroke", "#ffffff").attr("stroke-width", 0.8); hideTooltip(); });

    let canaryRegion = null;
    if (canFeature) {
      const canBounds = path.bounds(canFeature);
      const canW = Math.max(1, canBounds[1][0] - canBounds[0][0]);
      const canH = Math.max(1, canBounds[1][1] - canBounds[0][1]);
      const desiredW = compact ? Math.min(132, Math.max(86, width * 0.24)) : Math.min(150, Math.max(92, width * 0.15));
      const scale = desiredW / canW;
      const targetX = margin.left + width * (compact ? 0.18 : 0.14);
      const targetY = height - margin.bottom - Math.max(compact ? 70 : 78, canH * scale * 0.7);
      const tx = targetX - canBounds[0][0] * scale;
      const ty = targetY - canBounds[0][1] * scale;
      const canPath = svg.append("g").attr("transform", `translate(${tx},${ty}) scale(${scale})`);
      canaryRegion = canPath.append("path")
        .datum(canFeature)
        .attr("class", "ced-map-region")
        .attr("data-ced-region", "Canarias")
        .attr("d", path)
        .attr("fill", fillFor("Canarias"))
        .attr("stroke", "#17212b")
        .attr("stroke-width", 1.1 / scale)
        .attr("cursor", "pointer")
        .on("pointermove", function(event) {
          d3.select(this).attr("stroke-width", 2.4 / scale);
          showTooltip(event, "Canarias", tooltipValue(valueLabel(state.metric, values.get("Canarias"))));
        })
        .on("pointerleave", function() { d3.select(this).attr("stroke-width", 1.1 / scale); hideTooltip(); });
      svg.append("text").attr("x", targetX + desiredW / 2).attr("y", targetY - 8).attr("text-anchor", "middle").attr("fill", "#17212b").attr("font-size", 12).attr("font-weight", 800).text("Canarias");
    }

    const missing = state.geojson.features.map(geoName).filter(name => !["Ceuta", "Melilla"].includes(name) && !values.has(normalizeCcaaName(name)));
    if (missing.length) {
      const missingText = compact ? `Sin dato: ${missing.length} territorios` : `Sin dato para ${currentPeriodLabel()}: ${missing.join(", ")}`;
      svg.append("text").attr("x", margin.left).attr("y", height - 12).attr("fill", "#657383").attr("font-size", 11).text(missingText);
    }

    const legendWidth = compact ? Math.min(width - 32, 280) : Math.min(360, width - 70);
    const legendX = compact ? 16 : width - legendWidth - 26;
    const legendY = height - 34;
    function highlightMapMembers(names) {
      const selected = new Set(names.map(normalizeCcaaName));
      mainlandPaths
        .attr("opacity", d => selected.has(normalizeCcaaName(geoName(d))) ? 1 : 0.16)
        .attr("stroke", d => selected.has(normalizeCcaaName(geoName(d))) ? "#17212b" : "#ffffff")
        .attr("stroke-width", d => selected.has(normalizeCcaaName(geoName(d))) ? 1.8 : 0.7);
      if (canaryRegion) {
        canaryRegion
          .attr("opacity", selected.has("Canarias") ? 1 : 0.16)
          .attr("stroke", selected.has("Canarias") ? "#17212b" : "#ffffff");
      }
    }
    function resetMapHighlight() {
      mainlandPaths.attr("opacity", 1).attr("stroke", "#ffffff").attr("stroke-width", 0.8);
      if (canaryRegion) canaryRegion.attr("opacity", 1).attr("stroke", "#17212b");
    }

    const legendColors = uniqueValues.length > 1 ? mapPalette : [mapPalette[Math.floor(mapPalette.length / 2)]];
    const legendBins = legendColors.map((legendColor, index) => {
      const range = color.invertExtent ? color.invertExtent(legendColor) : extent;
      const members = rows.filter(d => color(d[state.metric]) === legendColor).sort((a, b) => d3.descending(a[state.metric], b[state.metric]));
      const min = range[0] ?? extent[0];
      const max = range[1] ?? extent[1];
      return { color: legendColor, index, min, max, members };
    });
    const segmentWidth = legendWidth / legendColors.length;
    svg.append("g").selectAll("rect").data(legendBins).join("rect")
      .attr("x", (d, i) => legendX + i * segmentWidth)
      .attr("y", legendY)
      .attr("width", Math.ceil(segmentWidth))
      .attr("height", 10)
      .attr("rx", (d, i) => i === 0 || i === legendBins.length - 1 ? 4 : 0)
      .attr("fill", d => d.color)
      .attr("cursor", "pointer")
      .on("pointermove", function(event, d) {
        const names = d.members.map(row => row.ccaa);
        highlightMapMembers(names);
        d3.select(this).attr("stroke", "#17212b").attr("stroke-width", 1.3);
        const rangeText = `${valueLabel(state.metric, d.min)} - ${valueLabel(state.metric, d.max)}`;
        const listText = names.length ? names.join(", ") : "Sin comunidades en este tramo";
        showTooltip(event, `Rango ${d.index + 1}`, `${tooltipValue(rangeText)}${listText}`);
      })
      .on("pointerleave", function() {
        d3.select(this).attr("stroke", null).attr("stroke-width", null);
        resetMapHighlight();
        hideTooltip();
      });
    svg.append("text").attr("x", legendX).attr("y", legendY - 7).attr("fill", "#657383").attr("font-size", compact ? 11 : 12).text(`${compact ? meta.short : meta.label} (${meta.unit})`);
    svg.append("text").attr("x", legendX + legendWidth).attr("y", legendY - 7).attr("text-anchor", "end").attr("fill", "#657383").attr("font-size", compact ? 10 : 11).text(uniqueValues.length > 1 ? "cuantiles" : "valor único");
    svg.append("text").attr("x", legendX).attr("y", legendY + 26).attr("fill", "#657383").attr("font-size", 12).text(valueLabel(state.metric, extent[0]));
    svg.append("text").attr("x", legendX + legendWidth).attr("y", legendY + 26).attr("text-anchor", "end").attr("fill", "#657383").attr("font-size", 12).text(valueLabel(state.metric, extent[1]));
  }

  function renderContextFallback() {
    els.sub.textContent = "No se pudo cargar la geometría del mapa; se muestra ranking autonómico como respaldo.";
    const rows = validRows(state.metric).sort((a, b) => d3.descending(a[state.metric], b[state.metric]));
    const { width, height } = chartSize();
    const compact = isCompactLayout();
    const margin = compact ? { top: 18, right: 12, bottom: 42, left: 102 } : { top: 18, right: 22, bottom: 42, left: 150 };
    const svg = d3.select(els.chart).append("svg").attr("viewBox", [0, 0, width, height]);
    const x = d3.scaleLinear().domain([0, d3.max(rows, d => d[state.metric]) || 1]).nice().range([margin.left, width - margin.right]);
    const y = d3.scaleBand().domain(rows.map(d => d.ccaa)).range([margin.top, height - margin.bottom]).padding(0.22);
    svg.append("g").attr("class", "ced-axis").attr("transform", `translate(0,${height - margin.bottom})`).call(d3.axisBottom(x).ticks(5).tickFormat(d => metricMeta[state.metric].format(displayValue(state.metric, d))));
    svg.append("g").attr("class", "ced-axis").attr("transform", `translate(${margin.left},0)`).call(d3.axisLeft(y).tickFormat(d => compact ? compactCcaaLabel(d) : d).tickSize(0)).call(g => g.select(".domain").remove());
    svg.selectAll("rect").data(rows).join("rect").attr("x", margin.left).attr("y", d => y(d.ccaa)).attr("width", d => Math.max(1, x(d[state.metric]) - margin.left)).attr("height", y.bandwidth()).attr("rx", 3).attr("fill", d => d.ccaa === "Canarias" ? "#1769aa" : "#b9c5d0").on("pointermove", (event, d) => showTooltip(event, d.ccaa, tooltipValue(valueLabel(state.metric, d[state.metric])))).on("pointerleave", hideTooltip);
  }

  function renderEvolution() {
    const meta = metricMeta[state.metric];
    const sceneMeta = sceneById.get(state.mode);
    els.title.textContent = `Evolución: ${meta.label}`;
    els.sub.textContent = sceneMeta?.sub || "Todas las comunidades a través del tiempo. Pasa el ratón por una línea para aislarla y leer sus valores.";
    const rows = state.global.filter(d => d[state.metric] !== null);
    const series = Array.from(d3.group(rows, d => d.ccaa), ([ccaa, values]) => ({ ccaa, values: values.sort((a, b) => d3.ascending(a.periodo, b.periodo)) }));
    const { width, height } = chartSize();
    const compact = isCompactLayout();
    const margin = compact ? { top: 24, right: 18, bottom: 46, left: 46 } : { top: 24, right: 150, bottom: 42, left: 58 };
    const svg = d3.select(els.chart).append("svg").attr("viewBox", [0, 0, width, height]);
    const x = d3.scaleLinear().domain(d3.extent(rows, d => d.periodo)).range([margin.left, width - margin.right]);
    const y = d3.scaleLinear().domain(paddedExtent(rows.map(d => d[state.metric]), 0.08)).range([height - margin.bottom, margin.top]);
    const line = d3.line().defined(d => d[state.metric] !== null).x(d => x(d.periodo)).y(d => y(d[state.metric]));

    svg.append("g").attr("class", "ced-grid").attr("transform", `translate(${margin.left},0)`).call(d3.axisLeft(y).ticks(compact ? 4 : 5).tickSize(-(width - margin.left - margin.right)).tickFormat("")).call(g => g.select(".domain").remove());
    svg.append("g").attr("class", "ced-axis").attr("transform", `translate(0,${height - margin.bottom})`).call(d3.axisBottom(x).ticks(compact ? 4 : 8).tickFormat(d => Number.isInteger(d) ? d3.format("d")(d) : d3.format(".1f")(d)));
    svg.append("g").attr("class", "ced-axis").attr("transform", `translate(${margin.left},0)`).call(d3.axisLeft(y).ticks(compact ? 4 : 5).tickFormat(d => metricMeta[state.metric].format(displayValue(state.metric, d))));
    svg.append("text").attr("x", margin.left).attr("y", 14).attr("fill", "#657383").attr("font-size", 12).text(`${compact ? meta.short : meta.label} (${meta.unit})`);

    const lineLayer = svg.append("g");
    const labelLayer = svg.append("g");
    const hitLayer = svg.append("g");
    const paths = lineLayer.selectAll("path.ced-series").data(series).join("path")
      .attr("class", "ced-series ced-muted-line")
      .attr("d", d => line(d.values))
      .attr("fill", "none")
      .attr("stroke", d => d.ccaa === "Canarias" ? "#1769aa" : "#aab6c2")
      .attr("stroke-width", d => d.ccaa === "Canarias" ? 3.2 : 1.5)
      .attr("opacity", d => d.ccaa === "Canarias" ? 1 : 0.55);

    function highlight(name, event) {
      paths.attr("opacity", d => d.ccaa === name ? 1 : 0.12).attr("stroke-width", d => d.ccaa === name ? 3.8 : 1.1).attr("stroke", d => d.ccaa === name ? "#1769aa" : "#cbd4dd");
      labelLayer.selectAll("*").remove();
      const selected = series.find(d => d.ccaa === name);
      if (!selected) return;
      const last = selected.values[selected.values.length - 1];
      labelLayer.append("text").attr("x", compact ? width - margin.right - 4 : x(last.periodo) + 8).attr("y", y(last[state.metric])).attr("dy", "0.35em").attr("text-anchor", compact ? "end" : "start").attr("fill", "#1769aa").attr("font-size", compact ? 12 : 13).attr("font-weight", 800).text(compact ? compactCcaaLabel(name) : name);
      selected.values.forEach(d => labelLayer.append("circle").attr("cx", x(d.periodo)).attr("cy", y(d[state.metric])).attr("r", 4).attr("fill", "#1769aa"));
      const nearest = nearestPoint(selected.values, event, x);
      showTooltip(event, `${name} · ${rowPeriodLabel(nearest)}`, tooltipValue(valueLabel(state.metric, nearest[state.metric])));
    }

    function reset() {
      paths.attr("opacity", d => d.ccaa === "Canarias" ? 1 : 0.55).attr("stroke-width", d => d.ccaa === "Canarias" ? 3.2 : 1.5).attr("stroke", d => d.ccaa === "Canarias" ? "#1769aa" : "#aab6c2");
      labelLayer.selectAll("*").remove();
      const can = series.find(d => d.ccaa === "Canarias");
      if (can) {
        const last = can.values[can.values.length - 1];
        labelLayer.append("text").attr("x", compact ? width - margin.right - 4 : x(last.periodo) + 8).attr("y", y(last[state.metric])).attr("dy", "0.35em").attr("text-anchor", compact ? "end" : "start").attr("fill", "#1769aa").attr("font-size", compact ? 12 : 13).attr("font-weight", 800).text("Canarias");
      }
      hideTooltip();
    }

    hitLayer.selectAll("path.ced-line-hit").data(series).join("path")
      .attr("class", "ced-line-hit")
      .attr("d", d => line(d.values))
      .attr("fill", "none")
      .attr("stroke", "transparent")
      .attr("stroke-width", 14)
      .on("pointermove", (event, d) => highlight(d.ccaa, event))
      .on("pointerleave", reset);
    reset();
  }

  function nearestPoint(values, event, xScale) {
    const [mx] = d3.pointer(event, els.chart.querySelector("svg"));
    return d3.least(values, d => Math.abs(xScale(d.periodo) - mx)) || values[values.length - 1];
  }

  function renderGender() {
    const metric = state.metric;
    const sceneMeta = sceneById.get(state.mode);
    els.title.textContent = `Género: ${metricMeta[metric].label}`;
    els.sub.textContent = sceneMeta?.sub || `Comparación mujeres-hombres por comunidad en ${currentPeriodLabel(metric)}. Solo se muestran variables disponibles con desagregación por género.`;
    const rows = genderGapRows(metric).sort((a, b) => d3.descending(Math.abs(a.gap), Math.abs(b.gap)));
    const { width, height } = chartSize();
    const compact = isCompactLayout();
    const margin = compact ? { top: 42, right: 52, bottom: 44, left: 96 } : { top: 38, right: 118, bottom: 42, left: 150 };
    const svg = d3.select(els.chart).append("svg").attr("viewBox", [0, 0, width, height]);
    const extent = d3.extent(rows.flatMap(d => [d.men, d.women]));
    const x = d3.scaleLinear().domain(extent).nice().range([margin.left, width - margin.right]);
    const y = d3.scaleBand().domain(rows.map(d => d.ccaa)).range([margin.top, height - margin.bottom]).padding(0.36);
    svg.append("g").attr("class", "ced-grid").attr("transform", `translate(0,${height - margin.bottom})`).call(d3.axisBottom(x).ticks(compact ? 4 : 5).tickSize(-(height - margin.top - margin.bottom)).tickFormat("")).call(g => g.select(".domain").remove());
    svg.append("g").attr("class", "ced-axis").attr("transform", `translate(0,${height - margin.bottom})`).call(d3.axisBottom(x).ticks(compact ? 4 : 5).tickFormat(d => metricMeta[metric].format(displayValue(metric, d))));
    svg.append("g").attr("class", "ced-axis").attr("transform", `translate(${margin.left},0)`).call(d3.axisLeft(y).tickFormat(d => compact ? compactCcaaLabel(d) : d).tickSize(0)).call(g => g.select(".domain").remove());
    const rowLayer = svg.append("g");
    const rowGroups = rowLayer.selectAll("g.ced-gender-row").data(rows).join("g").attr("class", "ced-gender-row").attr("cursor", "pointer");
    rowGroups.append("line").attr("x1", d => x(d.men)).attr("x2", d => x(d.women)).attr("y1", d => y(d.ccaa) + y.bandwidth() / 2).attr("y2", d => y(d.ccaa) + y.bandwidth() / 2).attr("stroke", d => d.ccaa === "Canarias" ? "#17212b" : "#c9d2db").attr("stroke-width", d => d.ccaa === "Canarias" ? 2.4 : 1.7);
    rowGroups.append("circle").attr("class", "ced-men-dot").attr("cx", d => x(d.men)).attr("cy", d => y(d.ccaa) + y.bandwidth() / 2).attr("r", d => d.ccaa === "Canarias" ? 5 : 4).attr("fill", "#168a81");
    rowGroups.append("circle").attr("class", "ced-women-dot").attr("cx", d => x(d.women)).attr("cy", d => y(d.ccaa) + y.bandwidth() / 2).attr("r", d => d.ccaa === "Canarias" ? 5 : 4).attr("fill", "#c84f3f");
    rowGroups.append("text").attr("x", compact ? width - 4 : width - margin.right + 18).attr("y", d => y(d.ccaa) + y.bandwidth() / 2).attr("dy", "0.35em").attr("text-anchor", compact ? "end" : "start").attr("fill", d => d.ccaa === "Canarias" ? "#1769aa" : "#657383").attr("font-weight", d => d.ccaa === "Canarias" ? 800 : 500).attr("font-size", compact ? 11 : 12).text(d => deltaLabel(metric, d.gap));
    rowGroups.append("rect").attr("x", compact ? 0 : margin.left).attr("y", d => y(d.ccaa) - 4).attr("width", compact ? width : width - margin.left - margin.right + 100).attr("height", y.bandwidth() + 8).attr("fill", "transparent")
      .on("pointermove", function(event, d) {
        rowGroups.attr("opacity", r => r.ccaa === d.ccaa ? 1 : 0.22);
        d3.select(this.parentNode).raise().select("line").attr("stroke", "#1769aa").attr("stroke-width", 3.2);
        d3.select(this.parentNode).selectAll("circle").attr("r", 6);
        showTooltip(event, d.ccaa, `Brecha${tooltipValue(valueLabel(metric, d.gap))}Mujeres: ${valueLabel(metric, d.women)}<br>Hombres: ${valueLabel(metric, d.men)}`);
      })
      .on("pointerleave", function() {
        rowGroups.attr("opacity", 1);
        rowGroups.select("line").attr("stroke", d => d.ccaa === "Canarias" ? "#17212b" : "#c9d2db").attr("stroke-width", d => d.ccaa === "Canarias" ? 2.4 : 1.7);
        rowGroups.select(".ced-men-dot").attr("r", d => d.ccaa === "Canarias" ? 5 : 4);
        rowGroups.select(".ced-women-dot").attr("r", d => d.ccaa === "Canarias" ? 5 : 4);
        hideTooltip();
      });
    svg.append("circle").attr("cx", margin.left).attr("cy", 16).attr("r", 4).attr("fill", "#168a81");
    svg.append("text").attr("x", margin.left + 9).attr("y", 20).attr("font-size", 12).attr("fill", "#657383").text("Hombres");
    svg.append("circle").attr("cx", margin.left + 85).attr("cy", 16).attr("r", 4).attr("fill", "#c84f3f");
    svg.append("text").attr("x", margin.left + 94).attr("y", 20).attr("font-size", 12).attr("fill", "#657383").text("Mujeres");
  }

  function renderMethod() {
    const sceneMeta = sceneById.get(state.mode);
    els.title.textContent = sceneMeta?.title || "Transparencia metodológica";
    els.sub.textContent = sceneMeta?.sub || "La pieza prioriza Supabase y conserva la geometría con respaldo remoto para no romper la visualización.";
    els.chart.style.display = "none";
    els.methodGrid.hidden = false;
    els.badge.textContent = "Reproducible";
  }

  function geoName(feature) {
    const raw = feature.properties?.NAME_LATN || feature.properties?.NUTS_NAME || feature.properties?.name || "";
    return normalizeCcaaName(raw);
  }

  function showTooltip(event, title, body) {
    els.tooltip.innerHTML = `<strong>${title}</strong><span class="ced-tooltip-metric">${tooltipMetricLabel()}</span>${body}`;
    els.tooltip.style.left = `${event.clientX}px`;
    els.tooltip.style.top = `${event.clientY}px`;
    els.tooltip.style.opacity = 1;
  }
  function hideTooltip() { els.tooltip.style.opacity = 0; }

  function downloadFilteredCsv() {
    const rows = state.global.filter(d => d[state.metric] !== null).map(d => ({
      ccaa: d.ccaa,
      periodo: d.periodo_key,
      periodo_label: rowPeriodLabel(d),
      origen: selectedMetricOrigin(d),
      indicador: state.metric,
      valor: d[state.metric],
    }));
    const csv = d3.csvFormat(rows);
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${topic.id}_${state.metric}_${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  }

  async function fetchSupabaseTable(table, schema = SUPABASE_CONFIG.dataSchema) {
    const pageSize = 1000;
    const rows = [];
    for (let offset = 0; ; offset += pageSize) {
      const response = await fetch(`${SUPABASE_CONFIG.url}/rest/v1/${encodeURIComponent(table)}?select=*&limit=${pageSize}&offset=${offset}`, {
        headers: {
          apikey: SUPABASE_CONFIG.anonKey,
          Authorization: `Bearer ${SUPABASE_CONFIG.anonKey}`,
          "Accept-Profile": schema,
        },
      });
      if (!response.ok) throw new Error(`Supabase ${table}: ${response.status}`);
      const page = await response.json();
      rows.push(...page);
      if (page.length < pageSize) break;
    }
    return rows;
  }

  // Hay dos formas de tabla en canendatos:
  //   * dos relaciones — <area>_global (género 'total') y <area>_gen (hombres y
  //     mujeres). Es lo que usan Dependencia, Educación, Empleo, Sanidad y Vivienda.
  //   * una sola relación con la columna `genero` incluyendo 'total'. Es el caso
  //     de Salud mental (ced_saludmental).
  // Se distinguen porque en la segunda genderTable === globalTable. Sin partirla,
  // coalesceRows(global, ["ccaa","periodo_key"]) mezclaría las filas de hombres y
  // mujeres dentro de la serie global, en silencio y sin error visible.
  function esFilaDeGenero(row) {
    return ["hombre", "mujer"].includes(normalizeGender(row.genero));
  }

  async function loadData() {
    const globalRows = await fetchSupabaseTable(topic.data.globalTable);

    if (includeGender && topic.data.genderTable === topic.data.globalTable) {
      return {
        global: globalRows.filter(row => !esFilaDeGenero(row)).map(parseRow),
        gender: globalRows.filter(esFilaDeGenero).map(parseGender),
      };
    }

    const parsedGlobal = globalRows.map(parseRow);
    let parsedGender = [];
    if (includeGender) {
      try {
        const genderRows = await fetchSupabaseTable(topic.data.genderTable);
        parsedGender = genderRows.map(parseGender);
      } catch (error) {
        console.warn(`[CED ${topic.id}] No se pudo cargar ${topic.data.genderTable}:`, error);
      }
    }
    return { global: parsedGlobal, gender: parsedGender };
  }

  async function fetchSupabaseGeo() {
    const table = topic.data.geoTable || "ccaa";
    const nameCol = topic.data.geoNameColumn || "ccaa";
    const geomCol = topic.data.geoGeometryColumn || "geom";
    const response = await fetch(`${SUPABASE_CONFIG.url}/rest/v1/${encodeURIComponent(table)}?select=${encodeURIComponent(nameCol)},${encodeURIComponent(geomCol)}`, {
      headers: {
        apikey: SUPABASE_CONFIG.anonKey,
        Authorization: `Bearer ${SUPABASE_CONFIG.anonKey}`,
        "Accept-Profile": SUPABASE_CONFIG.geoSchema,
      },
    });
    if (!response.ok) throw new Error(`Supabase geo ${table}: ${response.status}`);
    const rows = await response.json();
    const features = rows.map(row => {
      const geometry = typeof row[geomCol] === "string" ? JSON.parse(row[geomCol]) : row[geomCol];
      return { type: "Feature", properties: { NAME_LATN: normalizeCcaaName(row[nameCol]), NUTS_NAME: normalizeCcaaName(row[nameCol]) }, geometry };
    }).filter(f => f.geometry && !["Ceuta", "Melilla"].includes(geoName(f)));
    return { type: "FeatureCollection", features };
  }

  async function loadGeoJson() {
    try {
      return await fetchSupabaseGeo();
    } catch (error) {
      console.warn(`[CED ${topic.id}] No se pudo cargar geometría desde geodesocan, probando fallback`, error);
    }
    try {
      const response = await fetch(GEO_FALLBACK.geojsonUrl);
      if (!response.ok) throw new Error(response.status);
      const geo = await response.json();
      const features = (geo.features || []).filter(f => f.properties?.CNTR_CODE === "ES" && !["Ceuta", "Melilla"].includes(geoName(f)));
      return { type: "FeatureCollection", features };
    } catch (error) {
      console.warn(`[CED ${topic.id}] No se pudo cargar GeoJSON fallback`, error);
      return null;
    }
  }

  function boot(global, gender, geojson) {
    state.global = coalesceRows(global, ["ccaa", "periodo_key"]);
    state.gender = includeGender ? coalesceRows(gender, ["ccaa", "periodo_key", "genero"]) : [];
    state.sourceMode = "supabase";
    state.geojson = geojson;
    setupControls();
    render();
    const onResize = () => render();
    window.addEventListener("resize", onResize);
    els.sourceText.textContent = topic.sourceText || "Fuente: Supabase · canendatos";
  }

  try {
    const [data, geojson] = await Promise.all([loadData(), loadGeoJson()]);
    boot(data.global, data.gender, geojson);
  } catch (error) {
    console.error(`[CED ${topic.id}] Error al cargar datos:`, error);
    els.chart.innerHTML = `<div class="ced-loading">No se pudieron cargar los datos de <strong>${escapeHtml(topic.label)}</strong>. Revisa la consola para más detalles.</div>`;
    throw error;
  }
}
