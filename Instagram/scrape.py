import instaloader
import json

L = instaloader.Instaloader()

# Masukkan informasi login Anda
# username = input("Masukkan nama pengguna: ")
# password = input("Masukkan kata sandi: ")

# # Login ke akun Instagram
# L.context.log("Logging in...")
# L.load_session_from_file(username)
# if not L.context.is_logged_in:
#     L.context.log("Login failed.")
#     L.context.log("Logging in...")
#     L.context.session = None
#     L.interactive_login(username)

# Masukkan nama pengguna dan kode postingan Instagram
username = input("Masukkan nama pengguna: ")
post_id = input("Masukkan kode postingan: ")
# Bz5T-14HJAZ

# Unduh informasi postingan
post = instaloader.Post.from_shortcode(L.context, post_id)

# Buat file untuk menyimpan komentar
filename = f"{username}_{post_id}_comments.json"
# with open(filename, "w", encoding="utf-8") as f:
#     # Unduh dan simpan komentar
#     for comment in post.get_comments():
#         comment_dict = {
#             "id": comment.id,
#             "created_at": comment.created_at_utc.strftime("%Y-%m-%d %H:%M:%S"),
#             "text": comment.text,
#             "owner_username": comment.owner.username
#         }
#         json.dump(comment_dict, f, ensure_ascii=False)
#         f.write("\n")