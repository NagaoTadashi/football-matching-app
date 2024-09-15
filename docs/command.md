# マイグレーションコマンド

## FastAPI 開発サーバーの起動

vicorn app.main:app --reload

## nuxt.js 開発サーバーの起動

npm run dev -- -o

## マイグレーションファイルの生成

alembic revision --autogenerate -m "Add new column to team model"

## マイグレーションの適用

alembic upgrade head
