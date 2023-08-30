# テキスト対話プラットフォーム
## 動作環境
Python 3.8.17

## 前提条件
- Amazon EC2インスタンスでnginxによるWebサーバ起動ができている
- /dialogueへのGETが許可されている

## 導入方法
- リポジトリをクローン

  ```
  git clone https://github.com/nu-dialogue/dialogue-platform.git
  ```
  
- ライブラリをインストール
  - GPT-3.5/4を使用することを想定しています
  - 他のモデルを使用する場合はそのモデルに応じたライブラリをインストールする必要があります

  ```
  pip install -r requirements.txt
  ```

- APIキーの設定
  - 環境変数`OPENAI_API_KEY`にOpenAIのAPIキーを設定

  ```
  export OPENAI_API_KEY="<自身のAPIキー>"
  ```

## ファイル構成
- `log/`: ログ出力用ディレクトリ
- `server.py`: Webサーバ管理用スクリプト
- `gpt_bot.py`: GPT-3.5/4による発話生成を行うスクリプト
- `interface.py`: 対話インタフェースのHTMLが記述されたスクリプト
- `start.sh`: 実行用シェルスクリプト

## 実行例
- 対話プラットフォームの起動

```
bash start.sh
```

