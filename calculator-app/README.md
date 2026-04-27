# 🧮 計算機小程式

一個功能齊全的網頁計算機小程式，支持基本四則運算、百分比計算、歷史記錄等功能。

## 🚀 功能特點

- **基本運算**：加減乘除
- **進階功能**：冪運算 (^)、開方 (√)、百分比 (%)、圓周率 (π)、自然對數底 (e)
- **滑動條輸入**：可透過滑動條快速輸入數字
- **計算歷史**：自動記錄計算過程和結果
- **鍵盤支援**：支持鍵盤輸入
- **響應式設計**：支持各種設備

## 📋 使用方法

### 網頁端
1. 部署後訪問提供的 URL
2. 在瀏覽器中輸入數字和運算符號
3. 點擊運算按鈕或按下 Enter 鍵計算結果
4. 查看計算歷史記錄

### API 端（可選）
```bash
# 安裝後端
pip install -r requirements.txt

# 啟動服務
python app.py

# 使用 API
curl -X POST -H "Content-Type: application/json" \
  -d '{"expression": "12 + 34 * 5"}' \
  http://localhost:5000/api/calculate
```

## 🛠️ 技術棧

- **前端**：HTML5, CSS3, JavaScript, math.js CDN
- **後端**：Flask, Flask-CORS
- **託管服務**：Railway（支持靜態頁面文件）

## 📸 預覽

![Calculator](https://via.placeholder.com/400x600.png?text=Calculator+Preview)

## 🐛 已知問題

- 沒有進行錯誤處理（ intentional for simplicity）
- 沒有添加密碼驗證（網頁計算機不需要）

## 📝 授權

MIT License

## 🙏 開發者

由 AI 助手自動生成
