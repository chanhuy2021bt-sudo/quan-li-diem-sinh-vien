
import streamlit as st
import pandas as pd

# 1. Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# 2. Tao du lieu 10 sinh vien
data = {
    "Ho_ten": [
        "Huy", "Khôi", "Duy", "Hải", "Khang", "An", "Vinh", "Việt", "Tín", "Huya"
    ],
    "Chuyen_can": [8, 9, 7, 6, 10, 8, 7, 5, 9, 6],
    "Giua_ky":    [7, 8, 6, 5, 9, 7, 6, 4, 8, 5],
    "Cuoi_ky":    [8, 9, 7, 6, 10, 8, 7, 5, 9, 6]
}

df = pd.DataFrame(data)

# 3. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# 4. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Tieu de website
st.title("QUAN LY DIEM SINH VIEN")
st.write("Ung dung quan ly ket qua hoc tap")

# 6. Hien thi bang diem
st.subheader("1. Bang diem sinh vien")

bang = df.rename(columns={
    "Ho_ten": "Ho ten",
    "Chuyen_can": "Chuyen can",
    "Giua_ky": "Giua ky",
    "Cuoi_ky": "Cuoi ky",
    "Tong_ket": "Tong ket",
    "Xep_loai": "Xep loai"
})

st.dataframe(bang.round(2), use_container_width=True)

# 7. Thong ke
st.subheader("2. Thong ke ket qua")

sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
diem_tb = df["Tong_ket"].mean()
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Diem trung binh", f"{diem_tb:.2f}")
c2.metric("Diem cao nhat", f"{sv_max['Tong_ket']:.2f}")
c3.metric("Diem thap nhat", f"{sv_min['Tong_ket']:.2f}")
c4.metric("So sinh vien dat", f"{so_sv_dat}/10")

st.write("Sinh vien cao nhat:", sv_max["Ho_ten"])
st.write("Sinh vien thap nhat:", sv_min["Ho_ten"])

# 8. Chon sinh vien
st.subheader("3. Tra cuu sinh vien")

ten = st.selectbox("Chon mot sinh vien", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Ho ten:", sv["Ho_ten"])
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", round(sv["Tong_ket"], 2))
st.write("Xep loai:", sv["Xep_loai"])

# 9. Bieu do cot
st.subheader("4. Bieu do diem tong ket")
st.bar_chart(df.set_index("Ho_ten")["Tong_ket"])

# 10. Thong tin nguoi tao
st.divider()
st.caption("Nguoi tao: Nguyễn Đạt Lâm Chấn Huy | MSSV: 17")
