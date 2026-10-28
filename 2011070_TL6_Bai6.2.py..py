# =========================================================================
# BÀI 2: HÀM CHUYỂN ĐỔI TIỀN TỆ ĐA QUỐC GIA
# Đặt tên file: 2011xxx_TL6_Bai2.py
# =========================================================================

def convert_currency(amount: float, from_currency: str, to_currency: str = "VND") -> float:
    """
    Chuyển đổi tiền tệ từ ngoại tệ sang VND (hoặc ngược lại dựa theo tỷ giá giả định).
    Tham số:
        amount (float): Số tiền cần chuyển đổi.
        from_currency (str): Mã loại tiền tệ gốc (ví dụ: "USD", "EUR", "JPY").
        to_currency (str): Mã loại tiền tệ đích (mặc định là "VND").
    Trả về:
        float: Số tiền sau khi chuyển đổi, hoặc -1 nếu loại tiền tệ không được hỗ trợ.
    """
    # Bảng tỷ giá giả định so với VND
    exchange_rates = {
        "USD": 25000.0,
        "EUR": 27000.0,
        "JPY": 160.0,
        "VND": 1.0
    }
    
    # Chuẩn hóa mã tiền tệ về chữ in hoa để so sánh chính xác
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    
    # Kiểm tra xem loại tiền tệ gốc và đích có được hỗ trợ hay không
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print(f"Lỗi: Mã tiền tệ không được hỗ trợ (from: {from_currency}, to: {to_currency})")
        return -1.0
    
    # Quy đổi trung gian qua VND: Số tiền gốc -> VND -> Tiền tệ đích
    amount_in_vnd = amount * exchange_rates[from_currency]
    result_amount = amount_in_vnd / exchange_rates[to_currency]
    
    return result_amount


# =========================================================================
# CHƯƠNG TRÌNH KIỂM THỬ (TEST CASES THEO YÊU CẦU)
# =========================================================================
print("=== THỰC HÀNH BÀI 2: CHUYỂN ĐỔI TIỀN TỆ ĐA QUỐC GIA ===")

# Test case 1: Chuyển 100 "USD" sang VND
val_1 = convert_currency(100, "USD")
print(f"Chuyển 100 USD -> Kết quả: {val_1:,.0f} VND")

# Test case 2: Chuyển 500 "EUR" sang VND
val_2 = convert_currency(500, "EUR")
print(f"Chuyển 500 EUR -> Kết quả: {val_2:,.0f} VND")

# Test case 3: Chuyển 1000 "AUD" (Không hỗ trợ)
val_3 = convert_currency(1000, "AUD")
print(f"Chuyển 1000 AUD -> Kết quả: {val_3}")
