#!/usr/bin/env python3
# rf_gain_block.py — SKiDL description of dual-band RF Gain Block
# pip install skidl


from skidl import Part, Net, ERC, generate_netlist

# 1. Reti
rf_in    = Net('RF_IN')
rf_out   = Net('RF_OUT')
gate     = Net('GATE')
drain    = Net('DRAIN')
vcc      = Net('VCC')
gnd      = Net('GND')

# 2. Filtri passa-banda (placeholder: footprint e libreria custom)
#    Creare in KiCad un symbol+footprint: Custom:BPF_2_4_5
BPF_IN   = Part('Custom', 'BPF_2_4_5', footprint='Custom:BPF_2_4_5')
BPF_OUT  = Part('Custom', 'BPF_2_4_5', footprint='Custom:BPF_2_4_5')

# 3. Componenti passivi matching ingresso
C1        = Part('Device', 'C', value='2pF', footprint='Capacitor_SMD:Cap_0402')
L_in      = Part('Device', 'L', value='2.8nH', footprint='Inductor_SMD:Ind_0402')
C_sh_in   = Part('Device', 'C', value='1.5pF', footprint='Capacitor_SMD:Cap_0402')

# 4. Bias e stadio attivo
R_g       = Part('Device', 'R', value='100k', footprint='Resistor_SMD:R_0603')
L_b       = Part('Device', 'L', value='220nH', footprint='Inductor_SMD:Ind_0603')
R_d       = Part('Device', 'R', value='50', footprint='Resistor_SMD:R_0603')
C_bypass  = Part('Device', 'C', value='100nF', footprint='Capacitor_SMD:Cap_0805')

# Q1 pHEMT
Q1        = Part('Qorvo_QPF4219', 'QPF4219', footprint='Qorvo_QPF4219:QPF4219_QFN16')

# 5. Componenti matching uscita
L_out     = Part('Device', 'L', value='3.2nH', footprint='Inductor_SMD:Ind_0402')
C2        = Part('Device', 'C', value='2pF', footprint='Capacitor_SMD:Cap_0402')
C_sh_out  = Part('Device', 'C', value='1.2pF', footprint='Capacitor_SMD:Cap_0402')

# 6. Collegamenti
# Ingresso RF → filtro → C1 → L_in → Gate
rf_in   += BPF_IN['IN']
BPF_IN['OUT']  += C1[1]
C1[2]  += L_in[1]
L_in[2] += gate

# Shunt ingresso
C_sh_in[1] += gate
C_sh_in[2] += gnd

# Gate bias
R_g[1]  += gate
R_g[2]  += gnd

# Drain bias
vcc     += L_b[1]
L_b[2]  += R_d[1]
R_d[2]  += drain
C_bypass[1] += drain
C_bypass[2] += gnd

# Connetto transistor
gate    += Q1['G']
drain   += Q1['D']
gnd     += Q1['S']  # source a massa
vcc     += Q1['VDD']  # Vdd

# Uscita: drain → L_out → C2 → BPF_OUT → RF_OUT
drain   += L_out[1]
L_out[2] += C2[1]
C2[2]   += BPF_OUT['IN']
BPF_OUT['OUT']  += rf_out

# Shunt uscita
C_sh_out[1] += rf_out
C_sh_out[2] += gnd

# 7. ERC e generazione netlist
ERC()
generate_netlist()  # crea rf_gain_block.net (KiCad compatibile)
