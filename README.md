【概要】 
chrome履歴から日本語辞書の検索記録をスクレイピング
---

※ 注意事項
・実行の時、ブラウザを終了しないとDBロックエラー発生。
⇒Chromeブラウザを終了しないとSQLiteで管理される履歴がロックされてる為、履歴を取得できない。


※ 使い方(google accountのエクスポート利用)
1. 環境に合わせてパラメータ設定(userConfig.py)：ファイルのパス以外には特に触らなくていい
2. BrowserHistory.json取得：google accountでchromeの履歴をエクスポート、「BrowserHistory.json」出力、配置
3. chromeを閉じてpython3でmain.py実行

※ シンボル
1. 覚えてない：'x'
2. 一回覚えたと思う：'1'
3. 覚えた：'o'
4. 間違った検索語：'-'

※ 重複チェック
・各グループ中で行う