CREATE TABLE public.sales_shops (
 num_shop int NULL,
 num_cash_desk int NULL,
 dt date NULL,
 doc_id varchar NULL,
 item varchar NULL,
 category varchar NULL,
 amount int NULL,
 price numeric NULL,
 discount int NULL
);

ALTER TABLE public.sales_shops ADD CONSTRAINT sales_shops_pk PRIMARY KEY (num_shop,num_cash_desk,dt,doc_id,item,category,amount,price,discount);