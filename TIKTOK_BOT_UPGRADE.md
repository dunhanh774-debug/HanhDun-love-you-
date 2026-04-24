# 🎬 TikTok Bot - Hướng Dẫn Sử Dụng Nâng Cấp

## 📋 Tính Năng Mới

### 1️⃣ **Xem Thông Tin Người Dùng** (`n lookup_tiktok`)

Lấy thông tin chi tiết về tài khoản TikTok

```
n lookup_tiktok username=quanlumiepro
```

**Output:**

- Tên hiển thị (nickname)
- Avatar người dùng
- Số followers / following / likes
- Bio
- Link trực tiếp đến tài khoản
- ✅ Badge nếu tài khoản được xác minh

---

### 2️⃣ **Xem Highlight Video** (`n highlight`)

Hiển thị 3 video có lượt thích cao nhất (Highlight)

```
n highlight username=quanlumiepro
```

**Output:**

- Danh sách 3 video nổi bật
- Hình ảnh bìa từng video
- Số lượng likes
- Link xem trực tiếp trên TikTok

---

### 3️⃣ **Tải Video TikTok** (`n getstory`)

Tải video trực tiếp (không logo) vào Discord

```
n getstory username=quanlumiepro index=1
```

**Tham số:**

- `username`: Tên TikTok user
- `index`: Video thứ mấy (1=mới nhất, mặc định=1)

**Output:**

- Video file (.mp4) được gửi trực tiếp vào Discord
- Thông tin: mô tả, lượt thích, bình luận, chia sẻ
- Nếu video > 25MB: Gửi link tải thay vì file

---

## 🔄 **Auto-Tracking (Tự Động Theo Dõi)**

Bot tự động quét các TikTok channel được chỉ định mỗi 30 phút.

### Cấu Hình:

1. **Tìm Channel ID Discord** của bạn (Enable Developer Mode)

2. **Chỉnh sửa trong `app.py`:**

```python
TIKTOK_TRACKED_CHANNELS = {
    "quanlumiepro": 1234567890,        # Thay bằng channel ID của bạn
    "tenbotiktok": 9876543210,         # Thêm các channel khác
}
```

3. **Bật Auto-Tracking:**
   - Tìm dòng: `# auto_track_tiktok.start()`
   - Bỏ `#` comment: `auto_track_tiktok.start()`

4. **Khi có highlight mới:**
   - Bot tự động ping @ role/channel
   - Gửi embed với thông tin video
   - Cập nhật cache tránh spam

### Ví dụ Hoạt Động:

```
[Mỗi 30 phút]
  → Kiểm tra @quanlumiepro có highlight mới?
  → Có? → Gửi embed vào #thong-bao
  → Không? → Chờ 30 phút tiếp theo
```

---

## 🛠️ **Thông Tin Kỹ Thuật**

### API Sử Dụng

- **tikwm.com**: API trung gian lấy dữ liệu TikTok
- **Ưu điểm:**
  - Không bị chặn như requests trực tiếp
  - Trả về JSON chuẩn
  - Hỗ trợ link tải không logo

### Hàm Backend

```python
get_tiktok_info(username)          # Lấy thông tin người dùng
get_tiktok_videos(username, count) # Lấy danh sách video
get_tiktok_highlights(username)    # Lấy video nổi bật
get_tiktok_video_download(...)     # Lấy link tải MP4
```

---

## ⚠️ **Lưu Ý**

1. **Kích thước Video:**
   - Discord limit = 25MB cho member bình thường
   - Nếu vượt: Bot gửi link thay vì file

2. **Rate Limiting:**
   - tikwm.com có thể chặn sau nhiều request liên tục
   - Nên thêm delay giữa các request nếu cần

3. **Error Handling:**
   - Tất cả hàm đều có try-except
   - Lỗi được in vào console để debug

---

## 📝 **Ví Dụ Sử Dụng Thực Tế**

### Scenario 1: Kiểm tra creator nổi tiếng

```
/lookup_tiktok username=khoa.phan
```

### Scenario 2: Xem video hot nhất

```
/highlight username=quanlumiepro
```

### Scenario 3: Tải video thứ 2 của ai đó

```
/getstory username=tenbotiktok index=2
```

### Scenario 4: Tự động theo dõi

- Config TIKTOK_TRACKED_CHANNELS
- Bật auto_track_tiktok.start()
- Bot sẽ ping khi có video mới

---

## 🚀 **Mở Rộng Tương Lai**

Có thể thêm:

- ✅ Tìm kiếm video theo từ khóa
- ✅ Thống kê xu hướng TikTok
- ✅ Tải nhiều video cùng lúc
- ✅ Filter video theo ngày/thời gian
- ✅ Lưu trữ video vào database

---

**Made with ❤️ for HanhDunLoveYou Bot**
