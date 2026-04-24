# ⚡ QUICK START - TikTok Bot Nâng Cấp

## 🚀 Bắt Đầu Nhanh

### ✅ Đã Upgrade:

- ✔️ `n lookup_tiktok` - Xem info TikTok user (cải thiện UI)
- ✔️ `n highlight` - Xem 3 video hot nhất
- ✔️ `n getstory` - Tải video TikTok không logo
- ✔️ Auto-tracking loop 30 phút

---

## 🎯 Các Lệnh Sử Dụng

### 1. Xem Thông Tin User

```
/lookup_tiktok username=<tên_tiktok>
```

✅ Kết quả: Embed với avatar, followers, bio, verified badge

### 2. Xem Video Hot Nhất

```
/highlight username=<tên_tiktok>
```

✅ Kết quả: 3 embeds với video có like nhiều nhất

### 3. Tải Video

```
/getstory username=<tên_tiktok> index=1
```

✅ Kết quả: Video MP4 được upload lên Discord

- `index=1` → video mới nhất
- `index=2` → video thứ 2
- v.v...

---

## ⚙️ Cấu Hình Auto-Tracking

### 📌 Bước 1: Lấy Channel ID

1. Mở Discord Settings → Advanced
2. Enable "Developer Mode"
3. Right-click channel → "Copy Channel ID"

### 📌 Bước 2: Cấu Hình trong app.py

Tìm đoạn code:

```python
TIKTOK_TRACKED_CHANNELS = {
    "quanlumiepro": 1234567890,  # Thay bằng channel ID của bạn
}
```

**Ví dụ:**

```python
TIKTOK_TRACKED_CHANNELS = {
    "quanlumiepro": 987654321,
    "khoaphann": 123456789,
}
```

### 📌 Bước 3: Bật Auto-Tracking

Tìm dòng cuối cùng:

```python
# auto_track_tiktok.start()
```

Bỏ comment bằng cách xóa `#`:

```python
auto_track_tiktok.start()
```

---

## 🧪 Test Features

```bash
# Test 1: Kiểm tra thông tin
/lookup_tiktok username=tiktok

# Test 2: Xem video hot
/highlight username=tiktok

# Test 3: Tải video
/getstory username=tiktok index=1
```

---

## ⚠️ Lưu Ý Quan Trọng

❗ **Video Limit:** Discord 25MB → Nếu video lớn, bot gửi link
❗ **Rate Limit:** Đừng spam requests → Có thể bị chặn tạm
❗ **Token:** Đảm bảo token Discord còn hiệu lực

---

## 🐛 Troubleshooting

| Vấn đề                     | Giải Pháp                             |
| -------------------------- | ------------------------------------- |
| Bot không phản hồi         | Check console xem lỗi gì, restart bot |
| Video không tải được       | Kiểm tra kích thước, thử user khác    |
| Auto-track không hoạt động | Kiểm tra channel ID, đã start() chưa? |
| Không tìm thấy video       | Username sai hoặc user không có video |

---

## 📚 File Tham Khảo

- **TIKTOK_BOT_UPGRADE.md** - Hướng dẫn chi tiết
- **app.py** - Source code (dòng ~3593-5270)

---

**🎉 Bây giờ bot của bạn đã hỗ trợ đầy đủ TikTok features!**
