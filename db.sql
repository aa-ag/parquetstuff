CREATE DATABASE parquet;

CREATE TABLE credit_record(
    id BIGINT,
    months_balance INTEGER,
    status VARCHAR(4)
);

\COPY credit_record FROM '../data/credit_record.csv' DELIMITER ',' CSV HEADER;