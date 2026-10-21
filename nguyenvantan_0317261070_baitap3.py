def stress_testing_matrix():
    # 1. Khởi tạo các tham số đầu vào
    V_goc = 20.0  # Giá trị danh mục gốc (đơn vị: Tỷ VNĐ)
    
    # Kịch bản Tỷ giá (ΔEx) và Lãi suất (ΔIr)
    list_delta_Ex = [-0.03, 0.00, 0.03]          # [-3%, 0%, +3%]
    list_delta_Ir = [-0.02, -0.01, 0.01, 0.02]    # [-2%, -1%, +1%, +2%]

    # 2. In tiêu đề ma trận (Các kịch bản Lãi suất)
    print("=" * 78)
    print("MA TRẬN MÔ PHỎNG GIÁ TRỊ DANH MỤC TẢI STRESS TEST (Đơn vị: Tỷ VNĐ)")
    print("=" * 78)
    
    # In hàng header chứa các mức biến động lãi suất
    header = f"{'ΔEx \\ ΔIr':<12} |"
    for d_Ir in list_delta_Ir:
        header += f" {d_Ir * 100:>+5.0f}%      |"
    print(header)
    print("-" * 78)

    # 3. Vòng lặp lồng nhau tính toán ma trận
    # Vòng lặp ngoài: Duyệt qua từng kịch bản Tỷ giá (ΔEx)
    for d_Ex in list_delta_Ex:
        row_str = f"Tỷ giá {d_Ex * 100:>+3.0f}% |"
        
        # Vòng lặp trong: Duyệt qua từng kịch bản Lãi suất (ΔIr)
        for d_Ir in list_delta_Ir:
            # Mô hình tính giá trị danh mục mới: V_mới = V_gốc * (1 + 1.5 * ΔEx - 2.0 * ΔIr)
            V_moi = V_goc * (1 + 1.5 * d_Ex - 2.0 * d_Ir)
            
            # Nối kết quả vào chuỗi hàng hiện tại
            row_str += f" {V_moi:>9.3f} Tỷ |"
            
        # In kết quả của cả hàng sau khi duyệt xong các kịch bản lãi suất
        print(row_str)

    print("-" * 78)

# Chạy chương trình
if __name__ == "__main__":
    stress_testing_matrix()
