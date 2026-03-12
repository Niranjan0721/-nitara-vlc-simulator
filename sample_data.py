# Sample data for VLC Simulator Windows GUI
# Same data as ESP32-S3 simulator

import random

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

# MA Sample Data - 5001 STIPL (receipt format matching real STIPL device)
def _fmt_stipl(code1, code2, mtype, name, qty, fat, snf, rate, shift, time_str):
    """Format STIPL receipt matching real milk analyzer output"""
    amount = qty * rate
    return (
        f"FIRM : KHATAL\n"
        f"1000209\n"
        f"NAYA GAUN\n"
        f"--------------\n"
        f"05/03/26({shift}) {time_str} !\n"
        f"CODE: {code1:2d} {code2:2d} -{mtype}\n"
        f"NAME: {name}\n"
        f"QTY : {qty:.2f} Lit.\n"
        f"FAT : {fat:.1f}  % *\n"
        f"SNF : {snf:.1f}  % *\n"
        f"RATE Rs. {rate:.2f}\n"
        f"AMOUNT Rs. {amount:.2f}\n"
        f"THANK YOU\n"
        f"--------------"
    )

ma_5001_samples = [
    _fmt_stipl(23, 22, "MIX", "", 1.78, 6.5, 9.0, 57.41, "E", "14:47"),
    _fmt_stipl(15, 8, "COW", "RAJESH", 10.25, 4.1, 8.7, 45.10, "M", "07:15"),
    _fmt_stipl(12, 5, "BUF", "SUNIL", 12.50, 7.2, 9.1, 50.25, "M", "07:30"),
    _fmt_stipl(18, 14, "MIX", "MAHESH", 15.00, 5.8, 8.2, 46.75, "E", "15:00"),
    _fmt_stipl(3, 27, "COW", "", 9.75, 4.5, 8.6, 44.90, "M", "08:10"),
    _fmt_stipl(20, 4, "BUF", "GANESH", 11.50, 6.8, 9.2, 51.75, "M", "08:25"),
    _fmt_stipl(10, 16, "MIX", "RAMESH", 8.50, 3.8, 8.5, 43.60, "E", "16:00"),
    _fmt_stipl(7, 19, "COW", "DINESH", 5.25, 4.3, 8.8, 44.50, "M", "06:45"),
    _fmt_stipl(25, 11, "BUF", "", 14.00, 7.5, 9.3, 52.00, "E", "15:30"),
    _fmt_stipl(1, 30, "MIX", "PRAKASH", 6.75, 5.2, 8.4, 46.00, "M", "07:00"),
    _fmt_stipl(28, 6, "COW", "VINOD", 11.00, 3.9, 8.6, 43.80, "M", "07:45"),
    _fmt_stipl(14, 21, "BUF", "ANIL", 13.25, 6.5, 9.0, 50.50, "E", "14:30"),
    _fmt_stipl(9, 3, "MIX", "", 7.00, 5.5, 8.3, 47.00, "M", "08:00"),
    _fmt_stipl(22, 17, "COW", "SANJAY", 8.75, 4.0, 8.7, 44.20, "E", "16:15"),
    _fmt_stipl(6, 28, "BUF", "MOHAN", 16.50, 7.0, 9.1, 51.25, "M", "06:30"),
    _fmt_stipl(30, 2, "MIX", "KISHAN", 4.50, 5.0, 8.5, 45.50, "M", "07:20"),
    _fmt_stipl(11, 24, "COW", "", 9.00, 4.2, 8.8, 44.75, "E", "15:45"),
    _fmt_stipl(16, 9, "BUF", "GOPAL", 12.00, 6.9, 9.2, 51.00, "M", "08:30"),
    _fmt_stipl(4, 13, "MIX", "RAVI", 7.25, 5.3, 8.4, 46.25, "E", "14:00"),
    _fmt_stipl(27, 20, "COW", "ASHOK", 10.50, 4.4, 8.9, 45.00, "M", "07:10"),
    _fmt_stipl(19, 7, "BUF", "", 13.75, 7.3, 9.0, 50.75, "M", "06:50"),
    _fmt_stipl(2, 26, "MIX", "VIJAY", 6.00, 5.7, 8.3, 47.50, "E", "16:30"),
    _fmt_stipl(21, 15, "COW", "DEEPAK", 8.25, 3.7, 8.6, 43.40, "M", "08:15"),
    _fmt_stipl(8, 1, "BUF", "NARESH", 14.50, 6.6, 9.1, 50.00, "E", "15:15"),
    _fmt_stipl(26, 10, "MIX", "", 5.75, 5.1, 8.5, 45.75, "M", "07:35"),
    _fmt_stipl(13, 29, "COW", "SURESH", 9.50, 4.6, 8.7, 45.25, "M", "06:40"),
    _fmt_stipl(17, 23, "BUF", "KAMAL", 11.75, 7.1, 9.3, 52.25, "E", "14:15"),
    _fmt_stipl(5, 18, "MIX", "PAVAN", 7.50, 5.4, 8.4, 46.50, "M", "08:05"),
    _fmt_stipl(29, 12, "COW", "", 10.00, 4.0, 8.8, 44.00, "E", "15:50"),
    _fmt_stipl(24, 8, "BUF", "HARISH", 15.25, 6.7, 9.2, 51.50, "M", "07:25"),
    _fmt_stipl(10, 25, "MIX", "LOKESH", 6.50, 5.6, 8.3, 47.25, "M", "06:55"),
    _fmt_stipl(20, 14, "COW", "GIRISH", 9.25, 4.3, 8.9, 44.60, "E", "16:05"),
    _fmt_stipl(15, 7, "BUF", "", 13.00, 7.4, 9.0, 50.50, "M", "08:20"),
]

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


def generate_ma_code_0000(model):
    """Generate MA code 0000 data with random values for all fields except code.
    Code is always 0000, but fat/snf/rate/amt/qty have realistic random values."""
    milk_types_receipt = ["Mix", "Cow", "Buffalo"]
    milk_types_stipl = ["MIX", "COW", "BUF"]
    shifts = ["M", "E"]

    qty = round(random.uniform(1.5, 18.0), 2)
    fat = round(random.uniform(3.5, 7.5), 2)
    snf = round(random.uniform(8.0, 9.5), 1)
    rate = round(random.uniform(40.0, 55.0), 2)
    amt = round(qty * rate, 2)
    clr = round(random.uniform(25.0, 35.0), 1)
    shift = random.choice(shifts)
    counter = random.randint(1, 10)

    # Receipt format (models 1001-2004)
    if 1001 <= model <= 2004:
        mt = random.choice(milk_types_receipt)
        return (
            f"Provisional Acknowldgement Slip\n\n"
            f"DIARY CRAFT PVT LTD\n\n"
            f"PEERNAGAR\n\n"
            f"MCC Code: MCC_001\n"
            f"VLCC Code: 00000215\n"
            f"Date: 05/12/23          Time: 07:01\n"
            f"Code: 0000\n"
            f"Name:\n"
            f"Milk Type: {mt}    Quantity: {qty:.2f}\n"
            f"FAT:      {fat:.2f}%   SNF:      {snf:.1f}%\n"
            f"Rate (Rs.): {rate:.2f}\n"
            f"Amount: {amt:.2f}\n"
            f"CLR: {clr:.1f}\n"
            f"Shift: {shift}    SSCounter: {counter}"
        )

    # Parentheses format (models 3001-3004)
    elif 3001 <= model <= 3004:
        # Format: (FFFSSSRRR...) - randomize values but code portion = 0000
        f_int = int(fat * 100)
        s_int = int(snf * 100)
        q_int = int(qty * 100)
        r_int = int(rate * 100)
        a_int = int(amt)
        return f"({f_int:04d}{s_int:04d}{r_int:04d}{q_int:04d}{clr*10:04.0f}{a_int:05d}0000{counter:03d}{shift})"

    # Newline format (models 4001-4003)
    elif 4001 <= model <= 4003:
        fat1 = round(random.uniform(3.0, 5.0), 2)
        snf1 = round(random.uniform(8.5, 9.5), 2)
        clr1 = round(random.uniform(28.0, 33.0), 2)
        return f"#{fat1:05.2f} {snf1:05.2f} {clr1:05.2f} {random.uniform(2.5, 4.0):05.2f} {random.uniform(4.0, 5.5):05.2f} {random.uniform(0.5, 0.8):05.2f} {random.uniform(29.0, 32.0):05.2f} {random.uniform(1.5, 2.5):05.2f} 00.00 0 0000 00.00 000.0"

    # STIPL format (model 5001)
    elif model == 5001:
        mt = random.choice(milk_types_stipl)
        time_str = f"{random.randint(6, 17):02d}:{random.randint(0, 59):02d}"
        return _fmt_stipl(0, 0, mt, "", qty, round(fat, 1), snf, rate, shift, time_str)

    # Fallback
    return generate_ma_code_0000(1001)

# Baud rates
BAUD_RATES = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
