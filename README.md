## Dự án chatbot365 (version 1.0)
`python+flask+rasa`
Author: Vũ Quang Cường
---------------------------
### Introduction
Chatbot365 ra đời nhằm mục đích giải đáp những vấn đề cơ bản nhất trong quá trình trợ giúp khách hàng khi sử dụng trang web timviec365.


Các chức năng chính là:
+ Tìm kiếm việc làm
+ Tìm kiếm ứng viên
+ Chào hỏi cơ bản (Xin chào, tạm biệt, vui , buồn)
+ Hỏi thông tin về bot (Tên, tuổi, địa chỉ, làm được gì)
---------------------------
### Cách cài đặt 

Sử dụng python 3.6 : conda create -n bots python=3.6

pip install -r requirement.txt
--------------------------
### Cách sử dụng
Lần đầu tiên sử dụng: 
gõ lệnh `rasa train`
1. Mở termial 1: rasa run -m models --enable-api
2. Mở termial 2: rasa run actions
3. Mở termial 3: python app.py (chạy flask)



