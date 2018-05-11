--
-- PostgreSQL database dump
--

-- Dumped from database version 10.3
-- Dumped by pg_dump version 10.3

-- Started on 2018-05-11 00:06:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2188 (class 1262 OID 16384)
-- Name: shutterfly_analytics; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE shutterfly_analytics WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';


ALTER DATABASE shutterfly_analytics OWNER TO postgres;

\connect shutterfly_analytics

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2189 (class 0 OID 0)
-- Dependencies: 2188
-- Name: DATABASE shutterfly_analytics; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE shutterfly_analytics IS 'Shutterfly coding challenge.';


--
-- TOC entry 1 (class 3079 OID 12278)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2191 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 196 (class 1259 OID 16385)
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    customer_id character varying(100) NOT NULL,
    event_time timestamp with time zone,
    last_name name,
    adr_city text,
    adr_state text
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- TOC entry 2192 (class 0 OID 0)
-- Dependencies: 196
-- Name: TABLE customer; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.customer IS 'Customer Table

';


--
-- TOC entry 197 (class 1259 OID 16391)
-- Name: image_upload; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.image_upload (
    image_id character varying(100) NOT NULL,
    event_time timestamp with time zone,
    customer_id character varying(100)
);


ALTER TABLE public.image_upload OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16394)
-- Name: order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."order" (
    order_id character varying(100) NOT NULL,
    event_time timestamp with time zone,
    customer_id character varying(100),
    total_amount character varying(50)
);


ALTER TABLE public."order" OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16506)
-- Name: site_visit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.site_visit (
    page_id character varying NOT NULL,
    customer_id character varying(100) NOT NULL,
    tags jsonb,
    event_time timestamp with time zone
);


ALTER TABLE public.site_visit OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16453)
-- Name: weekly_visit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weekly_visit (
    week_id character varying(100) NOT NULL,
    customer_id character varying(100) NOT NULL,
    week_start timestamp without time zone,
    week_end timestamp without time zone,
    weekly_total character varying(50),
    weekly_visits integer
);


ALTER TABLE public.weekly_visit OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16627)
-- Name: top_customer_ltv; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.top_customer_ltv AS
 WITH weeks AS (
         SELECT DISTINCT count(weekly_visit_1.week_id) AS number_of_weeks
           FROM public.weekly_visit weekly_visit_1
        )
 SELECT (sum((weekly_visit.weekly_total)::real) / (weeks.number_of_weeks)::double precision) AS average_weekly_revenue,
    weekly_visit.customer_id
   FROM public.weekly_visit,
    weeks
  GROUP BY weekly_visit.customer_id, weeks.number_of_weeks
  ORDER BY (sum((weekly_visit.weekly_total)::real) / (weeks.number_of_weeks)::double precision);


ALTER TABLE public.top_customer_ltv OWNER TO postgres;

--
-- TOC entry 2045 (class 2606 OID 16403)
-- Name: customer customer_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pk PRIMARY KEY (customer_id);


--
-- TOC entry 2048 (class 2606 OID 16401)
-- Name: image_upload image_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image_upload
    ADD CONSTRAINT image_pk PRIMARY KEY (image_id);


--
-- TOC entry 2052 (class 2606 OID 16413)
-- Name: order order_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pk PRIMARY KEY (order_id);


--
-- TOC entry 2057 (class 2606 OID 16513)
-- Name: site_visit page_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.site_visit
    ADD CONSTRAINT page_pk PRIMARY KEY (page_id);


--
-- TOC entry 2054 (class 2606 OID 16562)
-- Name: weekly_visit weekly_customer_ck; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weekly_visit
    ADD CONSTRAINT weekly_customer_ck PRIMARY KEY (week_id, customer_id);


--
-- TOC entry 2055 (class 1259 OID 16529)
-- Name: customer_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX customer_fk ON public.site_visit USING btree (customer_id);


--
-- TOC entry 2046 (class 1259 OID 16409)
-- Name: fki_customer_FK; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_customer_FK" ON public.image_upload USING btree (customer_id);


--
-- TOC entry 2049 (class 1259 OID 16419)
-- Name: fki_customer_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_customer_fk ON public."order" USING btree (customer_id);


--
-- TOC entry 2050 (class 1259 OID 16487)
-- Name: fki_site_customer_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_site_customer_fk ON public."order" USING btree (customer_id);


--
-- TOC entry 2058 (class 2606 OID 16404)
-- Name: image_upload customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image_upload
    ADD CONSTRAINT customer_fk FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


--
-- TOC entry 2059 (class 2606 OID 16414)
-- Name: order customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT customer_fk FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


--
-- TOC entry 2060 (class 2606 OID 16524)
-- Name: site_visit customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.site_visit
    ADD CONSTRAINT customer_fk FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


-- Completed on 2018-05-11 00:06:26

--
-- PostgreSQL database dump complete
--

