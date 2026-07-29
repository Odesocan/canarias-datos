from openpyxl import Workbook
import sys
wb = Workbook(); ws = wb.active; ws.title='Cap'
ws.append(['CCAA','1. Personal','2. Bienes','3. Financieros','4. Transferencias corrientes','6. Inversiones reales','7. Transferencias capital','8. Activos','9. Pasivos'])
for r in [('Andalucía',14500000000,4200000000,600000000,18000000000,2500000000,1200000000,200000000,1100000000),
          ('Canarias',3100000000,1100000000,250000000,4500000000,800000000,300000000,80000000,280000000),
          ('Cataluña',13800000000,4900000000,1200000000,17500000000,2200000000,950000000,300000000,4500000000)]:
    ws.append(r)
wb.save(sys.argv[1])
