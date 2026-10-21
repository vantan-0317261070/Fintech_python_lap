def dinh_gia_trai_phieu():
    # 1. Khởi tạo các thông số đầu vào
    F = 1000000.0     # Mệnh giá trái phiếu (VNĐ)
    c = 0.09          # Lãi suất coupon (9%/năm)
    N = 10            # Thời hạn trái phiếu (10 năm)
    y = 0.085         # Lợi suất kỳ vọng của thị trường (8.5%/năm)

    # 2. Tính số tiền lãi coupon hàng năm
    C = F * c

    # 3. Tính Giá trị hiện tại (PV) của từng khoản coupon bằng vòng lặp for
    tong_pv_coupon = 0.0
    
    print(f"{'Năm (t)':<10} | {'Lãi Coupon (VNĐ)':<20} | {'PV Coupon (VNĐ)':<20}")
    print("-" * 57)

    for t in range(1, N + 1):
        pv_c = C / ((1 + y) ** t)
        tong_pv_coupon += pv_c
        print(f"{t:<10} | {C:>20,.0f} | {pv_c:>20,.2f}")

    print("-" * 57)

    # 4. Tính Giá trị hiện tại (PV) của khoản nợ gốc nhận vào năm thứ 10
    pv_f = F / ((1 + y) ** N)

    # 5. Tính giá lý thuyết chuẩn của trái phiếu
    gia_trai_phieu = tong_pv_coupon + pv_f

    # 6. Xác định trạng thái giao dịch của trái phiếu
    if gia_trai_phieu > F:
        trang_thai = "Cao hơn mệnh giá (Premium)"
    elif gia_trai_phieu < F:
        trang_thai = "Thấp hơn mệnh giá (Discount)"
    else:
        trang_thai = "Đúng mệnh giá (Par)"

    # 7. In kết quả tổng hợp
    print("\n" + "=" * 50)
    print("BÁO CÁO KẾT QUẢ ĐỊNH GIÁ TRÁI PHIẾU")
    print("=" * 50)
    print(f"1. Số tiền lãi coupon trả hàng năm (C) : {C:,.0f} VNĐ")
    print(f"2. Tổng PV các khoản lãi coupon      : {tong_pv_coupon:,.2f} VNĐ")
    print(f"3. PV của mệnh giá gốc (năm 10)       : {pv_f:,.2f} VNĐ")
    print(f"4. Giá lý thuyết của trái phiếu (P0)  : {gia_trai_phieu:,.2f} VNĐ")
    print(f"-> Trạng thái định giá               : {trang_thai}")
    print("=" * 50)

# Chạy chương trình
if __name__ == "__main__":
    dinh_gia_trai_phieu()
