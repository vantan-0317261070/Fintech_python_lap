def mo_phong_huu_tri():
    # 1. Khởi tạo các thông số đầu vào
    tuoi = 25
    nam = 1
    so_du = 0.0
    tien_gui = 60000000.0        # 60 triệu VNĐ
    lai_suat = 0.10             # 10%/năm
    tang_tien_gui = 0.08        # 8%/năm
    muc_tieu = 10000000000.0    # 10 tỷ VNĐ

    # In tiêu đề bảng báo cáo
    print(f"{'Năm':<6} | {'Tuổi':<6} | {'Số tiền gửi mới (VNĐ)':<22} | {'Tiền lãi trong năm (VNĐ)':<24} | {'Tổng tài sản cuối năm (VNĐ)':<26}")
    print("-" * 95)

    # 2. Vòng lặp mô phỏng tích lũy
    while so_du < muc_tieu:
        # Tiền lãi tính trên số dư đầu kỳ
        tien_lai = so_du * lai_suat
        
        # Số dư cuối năm sau khi cộng tiền lãi và khoản gửi mới
        so_du = so_du + tien_lai + tien_gui
        
        # In tiến trình của năm hiện tại
        print(f"{nam:<6} | {tuoi:<6} | {tien_gui:>22,.0f} | {tien_lai:>24,.0f} | {so_du:>26,.0f}")
        
        # Cập nhật thông số cho năm tiếp theo
        tien_gui = tien_gui * (1 + tang_tien_gui)
        tuoi += 1
        nam += 1

    # 3. In kết quả tổng kết
    tuoi_dat_muck_tieu = tuoi - 1
    nam_tich_luy = nam - 1
    print("-" * 95)
    print(f"\n=> Kết luận:")
    print(f"- Người này đạt mục tiêu 10 tỷ VNĐ ở **{tuoi_dat_muck_tieu} tuổi**.")
    print(f"- Tổng thời gian tích lũy: **{nam_tich_luy} năm**.")

# Chạy chương trình
if __name__ == "__main__":
    mo_phong_huu_tri()
