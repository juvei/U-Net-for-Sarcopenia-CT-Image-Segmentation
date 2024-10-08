# step 1.
先將待處理圖片改名為 input.png 放在 input 資料夾內 (影像尺寸應大於1024x800)

# step 2.
執行 pre_process.py，結果會自動命名為 input.png 存放於 testing_set 資料夾中

# step 3.
執行 test.py，經處理過的圖片會命名為 result.jpg 存放於 result 資料夾中

# step 4.
執行 post_process，計算出 result.jpg的肌肉面積後印在terminal以及新視窗中
