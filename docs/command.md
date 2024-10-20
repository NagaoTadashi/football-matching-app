## FastAPI 開発サーバーの起動

vicorn app.main:app --reload

## nuxt.js 開発サーバーの起動

npm run dev -- -o

## データベース操作関係

# マイグレーションファイルの生成

alembic revision --autogenerate -m "コメント"

# マイグレーションの適用

alembic upgrade head
