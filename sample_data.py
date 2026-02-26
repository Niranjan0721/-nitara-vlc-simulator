# Sample data for VLC Simulator Windows GUI
# Same data as ESP32-S3 simulator

SAMPLE_DATA_COUNT = 33

# WM Models
WM_MODELS = {
    9001: "Type 1 Kg (+0017.31Kg)",
    9002: "Type 2 Lt (N0001.25=lt)",
    9003: "Type 3 Lt (L01234)",
    9004: "Type 4 Kg (00012)",
    9005: "Type 5 Lt (0123:)",
    9006: "Type 6 Kg (Custom)"
}

# MA Models
MA_MODELS = {
    1001: "Ekomilk Bond Standard (TIMEOUT+DPS)",
    1002: "Ekomilk Ultra DPS (TIMEOUT+DPS)",
    1003: "O-Right Ekomilk Ultra DPS (TIMEOUT+DPS)",
    1004: "Ekomilk Bond Lactoscan (TIMEOUT+DPS)",
    2001: "Ekomilk_Total (TIMEOUT)",
    2002: "Ekomilk_Horizon (TIMEOUT)",
    2003: "Ekomilk_Master (TIMEOUT)",
    2004: "Ekomilk_Master_Pro (TIMEOUT)",
    3001: "Speedy_with_paren (PARENTHESES)",
    3002: "Standard_with_paren (PARENTHESES)",
    3003: "Ultrasonic_with_paren (PARENTHESES)",
    3004: "Meko_with_paren (PARENTHESES)",
    4001: "Speedy_Newline (NEWLINE)",
    4002: "Standard_Newline (NEWLINE)",
    4003: "Ultrasonic_Newline (NEWLINE)",
    5001: "STIPL (TIMEOUT)"
}

# MA Detection Modes
MA_MODE_TIMEOUT = "TIMEOUT"
MA_MODE_PARENTHESES = "PARENTHESES"
MA_MODE_NEWLINE = "NEWLINE"

def get_ma_mode(model):
    """Get MA detection mode based on model number"""
    if 1001 <= model <= 2004:
        return MA_MODE_TIMEOUT
    elif 3001 <= model <= 3004:
        return MA_MODE_PARENTHESES
    elif 4001 <= model <= 4003:
        return MA_MODE_NEWLINE
    elif 5001 <= model <= 5001:
        return MA_MODE_TIMEOUT
    return MA_MODE_TIMEOUT

# WM Sample Data - Type 1 Kg
wm_type_1_kg = [
    "+0001.25Kg", "+0017.31Kg", "+0043.58Kg", "+0051.01Kg", "+0054.13Kg", "+0055.48Kg", "+0063.68Kg",
    "+0085.32Kg", "+0086.58Kg", "+0088.29Kg", "+0045.91Kg", "+0046.50Kg", "+0099.84Kg", "+0099.96Kg",
    "-0005.55Kg", "-0036.59Kg", "-0046.30Kg", "-0079.43Kg", "-0081.35Kg", "-0087.76Kg", "-0099.71Kg",
    "+0008.75Kg", "+0023.89Kg", "+0033.45Kg", "+0069.01Kg", "+0077.12Kg", "+0029.84Kg", "+0014.67Kg",
    "+0035.22Kg", "+0078.44Kg", "-0010.15Kg", "-0050.55Kg", "-0062.18Kg"
]

# WM Sample Data - Type 2 Lt
wm_type_2_lt = [
    "N0001.25=lt", "N0005.59=lt", "N0010.45=lt", "N0015.95=lt", "N0020.78=lt", "N0025.35=lt", "N0030.46=lt",
    "N0035.58=lt", "N0040.67=lt", "N0045.89=lt", "N0050.21=lt", "N0055.32=lt", "N0060.48=lt", "N0065.79=lt",
    "N0070.85=lt", "N0075.91=lt", "N0080.10=lt", "N0085.25=lt", "N0090.40=lt", "N0095.55=lt", "N0100.70=lt",
    "N0105.85=lt", "N0110.00=lt", "N0115.15=lt", "N0120.30=lt", "N0125.45=lt", "N0130.60=lt",
    "N0135.75=lt", "N0140.90=lt", "N0145.05=lt", "N0150.20=lt", "N0155.35=lt", "N0160.50=lt"
]

# WM Sample Data - Type 3 Lt
wm_type_3_lt = [
    "L01234", "L04567", "L08901", "L02345", "L06789", "L00123", "L04500", "L12345", "L08923", "L00234",
    "L04523", "L00678", "L05678", "L09123", "L01234", "L07890", "L04321", "L09876", "L03210", "L01112",
    "L04556", "L07878", "L02233", "L06777", "L04444", "L03333", "L01111", "L05555", "L08888", "L06666",
    "L04440", "L00345", "L00789"
]

# WM Sample Data - Type 4 Kg
wm_type_4_kg = [
    "00012", "00034", "00056", "00078", "00123", "00234", "00345", "00456", "00567", "00678",
    "00789", "00890", "00901", "00112", "00223", "00334", "00445", "00556", "00667", "00778",
    "00889", "00990", "00100", "00200", "00300", "00400", "00500", "00600", "00700", "00800",
    "00900", "00110", "00220"
]

# WM Sample Data - Type 5 Lt
wm_type_5_lt = [
    "0123:", "0456:", "0789:", "0123:", "0456:", "0789:", "0123:", "0456:", "0789:", "0123:",
    "0456:", "0789:", "0123:", "0456:", "0789:", "0123:", "0456:", "0789:", "0123:", "0456:",
    "0789:", "0123:", "0456:", "0789:", "0123:", "0456:", "0789:", "0123:", "0456:", "0789:",
    "0123:", "0456:", "0789:"
]

# WM Sample Data - Type 6 Kg (same as type 1)
wm_type_6_kg = wm_type_1_kg.copy()

# WM code 0000 data
wm_code_0000 = ["+0000.00Kg", "N0000.00=lt", "L00000", "00000", "0000:", "+0000.00Kg"]

# All WM samples by model
WM_SAMPLES = {
    9001: wm_type_1_kg,
    9002: wm_type_2_lt,
    9003: wm_type_3_lt,
    9004: wm_type_4_kg,
    9005: wm_type_5_lt,
    9006: wm_type_6_kg
}

WM_CODE_0000 = {
    9001: "+0000.00Kg",
    9002: "N0000.00=lt",
    9003: "L00000",
    9004: "00000",
    9005: "0000:",
    9006: "+0000.00Kg"
}

# MA Sample Data - 1001 Ekomilk Bond Standard (receipt format)
ma_1001_samples = [
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_001\nVLCC Code: 00000215\nDate: 05/12/23          Time: 07:01\nCode: 0011  10002150011\nName: \nMilk Type: Mix    Quantity: 7.86\nFAT:      6.36%   SNF:      8.4%\nRate (Rs.): 47.41\nAmount: 372.64\nCLR: 27.7\nShift: M    SSCounter: 3",
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_002\nVLCC Code: 00000216\nDate: 05/12/23          Time: 08:15\nCode: 0012  10002150012\nName: John Doe\nMilk Type: Cow    Quantity: 10.25\nFAT:      4.10%   SNF:      8.7%\nRate (Rs.): 45.10\nAmount: 461.02\nCLR: 29.2\nShift: M    SSCounter: 4",
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_003\nVLCC Code: 00000217\nDate: 05/12/23          Time: 09:45\nCode: 0013  10002150013\nName: Jane Smith\nMilk Type: Buffalo    Quantity: 12.50\nFAT:      7.20%   SNF:      9.1%\nRate (Rs.): 50.25\nAmount: 628.13\nCLR: 31.0\nShift: E    SSCounter: 1",
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_004\nVLCC Code: 00000218\nDate: 05/12/23          Time: 10:30\nCode: 0014  10002150014\nName: David Johnson\nMilk Type: Mix    Quantity: 15.00\nFAT:      5.80%   SNF:      8.2%\nRate (Rs.): 46.75\nAmount: 701.25\nCLR: 28.5\nShift: E    SSCounter: 2",
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_005\nVLCC Code: 00000219\nDate: 05/12/23          Time: 11:00\nCode: 0015  10002150015\nName: Emily Davis\nMilk Type: Cow    Quantity: 9.75\nFAT:      4.50%   SNF:      8.6%\nRate (Rs.): 44.90\nAmount: 438.78\nCLR: 30.0\nShift: M    SSCounter: 5",
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_006\nVLCC Code: 00000220\nDate: 05/12/23          Time: 11:30\nCode: 0016  10002150016\nName: Michael Brown\nMilk Type: Cow    Quantity: 8.50\nFAT:      3.80%   SNF:      8.5%\nRate (Rs.): 43.60\nAmount: 370.60\nCLR: 29.8\nShift: M    SSCounter: 6",
    "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_007\nVLCC Code: 00000221\nDate: 05/12/23          Time: 12:00\nCode: 0017  10002150017\nName: Sarah Johnson\nMilk Type: Buffalo    Quantity: 11.50\nFAT:      6.80%   SNF:      9.2%\nRate (Rs.): 51.75\nAmount: 595.12\nCLR: 32.1\nShift: E    SSCounter: 7",
] + ["Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_008\nVLCC Code: 00000222\nDate: 05/12/23          Time: 12:30\nCode: 0018  10002150018\nName: Test User\nMilk Type: Mix    Quantity: 10.00\nFAT:      5.00%   SNF:      8.5%\nRate (Rs.): 45.00\nAmount: 450.00\nCLR: 28.0\nShift: M    SSCounter: 8"] * 26

# MA Sample Data - 3001 Parentheses format
ma_3001_samples = [
    "(063004401090154056300300019000400227M)",
    "(072504501180164065300310020000410317M)",
    "(058004201070144045290290018000380197M)",
    "(065504301130174062310330021000450287M)",
    "(071504701150184068320320022000470347M)",
    "(060004001060134043280280017000360157M)",
    "(069504601120154058300300019000400237M)",
] + ["(063504401100154055300300019000410227M)"] * 26

# MA Sample Data - 4001 Newline format
ma_4001_samples = [
    "#03.50 08.80 30.20 03.10 04.70 00.64 30.60 01.90 00.00 0 0001 00.00 000.0",
    "#04.20 08.90 31.00 03.20 04.80 00.65 31.00 02.00 00.00 0 0002 00.00 000.0",
    "#03.80 08.70 29.80 03.00 04.60 00.63 30.20 01.85 00.00 0 0003 00.00 000.0",
    "#04.50 09.00 32.00 03.30 04.90 00.66 31.50 02.10 00.00 0 0004 00.00 000.0",
    "#03.60 08.60 29.50 02.90 04.50 00.62 29.80 01.80 00.00 0 0005 00.00 000.0",
    "#04.00 08.80 30.50 03.10 04.70 00.64 30.80 01.95 00.00 0 0006 00.00 000.0",
    "#04.30 08.95 31.20 03.25 04.85 00.65 31.20 02.05 00.00 0 0007 00.00 000.0",
] + ["#04.00 08.80 30.00 03.00 04.70 00.64 30.50 01.90 00.00 0 0008 00.00 000.0"] * 26

# MA Sample Data - 5001 STIPL (receipt format)
ma_5001_samples = [
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE:  6  3  -MIX\nNAME: CUST 006\nQTY:  7.50 Lit.\nFAT:  6.3  %\nSNF:  8.4  %\nRATE  Rs. 47.41\nAMOUNT Rs.  355.58\n-----------------------",
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE:  8  1  -COW\nNAME: CUST 012\nQTY: 10.25 Lit.\nFAT:  4.1  %\nSNF:  8.7  %\nRATE  Rs. 45.10\nAMOUNT Rs.  462.28\n-----------------------",
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE: 12  5  -BUF\nNAME: CUST 003\nQTY: 12.50 Lit.\nFAT:  7.2  %\nSNF:  9.1  %\nRATE  Rs. 50.25\nAMOUNT Rs.  628.13\n-----------------------",
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(E)\nCODE: 15  2  -MIX\nNAME: CUST 019\nQTY: 15.00 Lit.\nFAT:  5.8  %\nSNF:  8.2  %\nRATE  Rs. 46.75\nAMOUNT Rs.  701.25\n-----------------------",
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(E)\nCODE:  3  7  -COW\nNAME: CUST 025\nQTY:  9.75 Lit.\nFAT:  4.5  %\nSNF:  8.6  %\nRATE  Rs. 44.90\nAMOUNT Rs.  437.78\n-----------------------",
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE: 20  4  -BUF\nNAME: CUST 008\nQTY: 11.50 Lit.\nFAT:  6.8  %\nSNF:  9.2  %\nRATE  Rs. 51.75\nAMOUNT Rs.  595.13\n-----------------------",
    "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE: 10  6  -MIX\nNAME: CUST 031\nQTY:  8.50 Lit.\nFAT:  3.8  %\nSNF:  8.5  %\nRATE  Rs. 43.60\nAMOUNT Rs.  370.60\n-----------------------",
] + ["M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE:  5  9  -COW\nNAME: CUST 015\nQTY: 10.00 Lit.\nFAT:  5.0  %\nSNF:  8.5  %\nRATE  Rs. 45.00\nAMOUNT Rs.  450.00\n-----------------------"] * 26

ma_code_0000_stipl = "M01225\nShri D.U.S.M.L.\n-----------------------\n26/02/26(M)\nCODE:  0  0  -MIX\nNAME: CUST 000\nQTY:  0.00 Lit.\nFAT:  0.0  %\nSNF:  0.0  %\nRATE  Rs.  0.00\nAMOUNT Rs.   0.00\n-----------------------"

# MA code 0000 samples
ma_code_0000_receipt = "Provisional Acknowldgement Slip\n\nDIARY CRAFT PVT LTD\n\nPEERNAGAR\n\nMCC Code: MCC_001\nVLCC Code: 00000215\nDate: 05/12/23          Time: 07:01\nCode: 0000\nName:\nMilk Type: Mix    Quantity: 0.00\nFAT:      0.00%   SNF:      0.0%\nRate (Rs.): 0.00\nAmount: 0.00\nCLR: 0.0\nShift: M    SSCounter: 0"
ma_code_0000_paren = "(000000000000000000000000000000000000M)"
ma_code_0000_newline = "#00.00 00.00 00.00 00.00 00.00 00.00 00.00 00.00 00.00 0 0000 00.00 000.0"

# All MA samples by model
MA_SAMPLES = {
    1001: ma_1001_samples,
    1002: ma_1001_samples,  # Same receipt format
    1003: ma_1001_samples,
    1004: ma_1001_samples,
    2001: ma_1001_samples,  # Use receipt for timeout models
    2002: ma_1001_samples,
    2003: ma_1001_samples,
    2004: ma_1001_samples,
    3001: ma_3001_samples,
    3002: ma_3001_samples,
    3003: ma_3001_samples,
    3004: ma_3001_samples,
    4001: ma_4001_samples,
    4002: ma_4001_samples,
    4003: ma_4001_samples,
    5001: ma_5001_samples
}

MA_CODE_0000 = {
    1001: ma_code_0000_receipt,
    1002: ma_code_0000_receipt,
    1003: ma_code_0000_receipt,
    1004: ma_code_0000_receipt,
    2001: ma_code_0000_receipt,
    2002: ma_code_0000_receipt,
    2003: ma_code_0000_receipt,
    2004: ma_code_0000_receipt,
    3001: ma_code_0000_paren,
    3002: ma_code_0000_paren,
    3003: ma_code_0000_paren,
    3004: ma_code_0000_paren,
    4001: ma_code_0000_newline,
    4002: ma_code_0000_newline,
    4003: ma_code_0000_newline,
    5001: ma_code_0000_stipl
}

# Baud rates
BAUD_RATES = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
