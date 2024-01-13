from sqlalchemy import create_engine


engine = create_engine(
    'postgresql+psycopg2://postgres:RjjhE@127.0.0.1:5433/test_db',
    echo=True,
    pool_size=5,
    max_overflow=10
)
