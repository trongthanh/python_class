# Python Class — Bài tập & Starter Code

Kho mã dành cho lớp Python cho trẻ em: mã khởi đầu để làm bài trên lớp,
bài tập và các tệp hỗ trợ lập trình bằng Sublime Text.

## Chọn bài học

- Nhánh **`one_piece`** chứa dự án game One Piece dùng **pygame-ce**.
- Các phiên bản starter theo tuần được đánh dấu bằng tag. Xem trang
  **[Releases](https://github.com/trongthanh/python_class/releases)** để tải
  tệp ZIP của đúng tuần học.
- Nhánh có thể được cập nhật cho bài tiếp theo. Muốn bắt đầu lại một bài cũ,
  hãy dùng tag hoặc bản ZIP tương ứng thay vì bản mới nhất của nhánh.

## Chạy game

Dùng Python 3 và pygame-ce đã cài trong lớp. Nếu máy chưa có pygame-ce:

```sh
python3 -m pip install pygame-ce
```

Trên Windows có thể dùng `py -3` thay cho `python3`.

Giải nén bài học vào một thư mục riêng, giữ nguyên thư mục `assets/` bên cạnh
các tệp Python. Mở terminal tại thư mục có `main.py`, rồi chạy:

```sh
python3 main.py
```

**Chạy `main.py`**, không chạy riêng `luffy.py`, `world.py` hay `frames.py`.
Các tệp đó là module được game sử dụng. Hướng dẫn và các mục `TODO` trong
starter cho biết phần cần hoàn thành. Hãy sao lưu bài trước khi chỉnh sửa.

## Các tệp trong dự án One Piece

| Tệp / thư mục | Nội dung |
|---|---|
| `main.py` | Điểm khởi chạy game, vòng lặp và sự kiện cửa sổ |
| `luffy.py` | Nhân vật Luffy, di chuyển và hoạt ảnh |
| `world.py` | Cảnh game, mặt đất và camera; xuất hiện từ bài cuộn cảnh |
| `frames.py` | Cấu hình khung hình và điểm neo của sprite |
| `spritesheet.py` | Cắt hình từ spritesheet và xử lý màu nền |
| `assets/` | Hình ảnh và ghi chú nguồn; xem `assets/CREDITS.md` nếu có |
| `support/` | Công cụ hỗ trợ trình soạn thảo, không phải mã chạy game |

Danh sách module có thể thay đổi theo tuần. Tôn trọng ghi chú nguồn và quyền
sử dụng tài nguyên đi kèm từng bài.

## Thư mục `support/`

### `Python Main.sublime-build`

**Mục đích:** nhấn Build khi đang sửa một module như `luffy.py` hoặc `world.py`
mà vẫn chạy `main.py` — không cần chuyển sang tab `main.py`.

#### Cài một lần trong Sublime Text

1. Chọn **Preferences → Browse Packages…** để mở thư mục Packages của Sublime.
2. Mở thư mục **`User`** trong đó.
3. Chép tệp **[`support/Python Main.sublime-build`](support/Python%20Main.sublime-build)**
   vào thư mục `User`. Không chép cả thư mục `support` vào `User`.
4. Quay lại Sublime, chọn **Tools → Build System → Python Main**.
5. Mở một tệp Python trong bài học, lưu các module vừa sửa, rồi nhấn:
   - **macOS:** `⌘B`
   - **Windows / Linux:** `Ctrl+B`

Ví dụ, khi đang sửa `luffy.py`:

```text
thu_muc_bai_hoc/
  main.py        ← tệp được chạy
  luffy.py       ← tab đang mở
  world.py
  assets/
```

Build system đặt thư mục làm việc là thư mục của tệp đang mở và chạy
`main.py` **trong cùng thư mục đó**. Vì vậy, nó cũng chọn đúng bài khi máy có
nhiều thư mục bài học. Nó **không tìm ngược lên thư mục cha**: nếu đang mở
module trong một thư mục con không có `main.py`, hãy Build từ một module nằm
cạnh `main.py`.

#### Chọn đúng Python

- macOS / Linux: mặc định dùng `python3`.
- Windows: mặc định dùng `py -3`.
- Python được chọn phải có pygame-ce. Nếu gặp lỗi `No module named pygame`,
  hãy cài pygame-ce vào đúng Python đó hoặc sửa `cmd` trong bản build system
  đã chép vào `Packages/User` để trỏ đến Python đang dùng trong lớp.
- Nếu dùng môi trường ảo, thay lệnh bằng đường dẫn đến Python của môi trường
  đó. Không dùng Python tích hợp bên trong Sublime để chạy game.

Ví dụ dùng Python của môi trường ảo trên macOS / Linux:

```json
"cmd": ["/duong/dan/den/.venv/bin/python", "-u", "$file_path/main.py"]
```

Trên Windows, sửa `cmd` bên trong mục `windows`; đường dẫn JSON cần dùng
`\\` thay cho `\`:

```json
"windows": {
    "cmd": ["C:\\duong\\dan\\.venv\\Scripts\\python.exe", "-u", "$file_path/main.py"]
}
```

Nếu Sublime không tìm thấy `python3` hoặc `py`, dùng đường dẫn đầy đủ đến
Python. Đóng cửa sổ game trước khi Build lại.

Tham khảo: [Sublime Text — Build Systems](https://www.sublimetext.com/docs/build_systems.html).
