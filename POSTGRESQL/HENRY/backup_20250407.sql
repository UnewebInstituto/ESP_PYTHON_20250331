toc.dat                                                                                             0000600 0004000 0002000 00000044657 14775027576 0014503 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP   	                    }            bd_ig_henry    16.3    16.3 A               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                    0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                    0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                    1262    94102    bd_ig_henry    DATABASE     �   CREATE DATABASE bd_ig_henry WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Venezuela.1252';
    DROP DATABASE bd_ig_henry;
                postgres    false         �            1259    94105 	   contactos    TABLE     �   CREATE TABLE public.contactos (
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);
    DROP TABLE public.contactos;
       public         heap    postgres    false                    0    0    TABLE contactos    COMMENT     D   COMMENT ON TABLE public.contactos IS 'Ejemplo de tabla secuencial';
          public          postgres    false    215         �            1259    94174 
   contactos1    TABLE     �   CREATE TABLE public.contactos1 (
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);
    DROP TABLE public.contactos1;
       public         heap    postgres    false         	           0    0    TABLE contactos1    COMMENT     B   COMMENT ON TABLE public.contactos1 IS 'Tabla con índice único';
          public          postgres    false    216         �            1259    94194 
   contactos2    TABLE     �   CREATE TABLE public.contactos2 (
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);
    DROP TABLE public.contactos2;
       public         heap    postgres    false         �            1259    94205 
   contactos3    TABLE       CREATE TABLE public.contactos3 (
    id integer NOT NULL,
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60) NOT NULL,
    cedula character varying(15) NOT NULL
);
    DROP TABLE public.contactos3;
       public         heap    postgres    false         
           0    0    TABLE contactos3    COMMENT     �   COMMENT ON TABLE public.contactos3 IS 'Ejemplo de tabla que contendrá clave primaria para un campo serial, identficado con el nombre id';
          public          postgres    false    219         �            1259    94204    contactos3_id_seq    SEQUENCE     �   CREATE SEQUENCE public.contactos3_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.contactos3_id_seq;
       public          postgres    false    219                    0    0    contactos3_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.contactos3_id_seq OWNED BY public.contactos3.id;
          public          postgres    false    218         �            1259    94226 
   contactos4    TABLE     �   CREATE TABLE public.contactos4 (
    id bigint NOT NULL,
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);
    DROP TABLE public.contactos4;
       public         heap    postgres    false         �            1259    94225    contactos4_id_seq    SEQUENCE     z   CREATE SEQUENCE public.contactos4_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.contactos4_id_seq;
       public          postgres    false    221                    0    0    contactos4_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.contactos4_id_seq OWNED BY public.contactos4.id;
          public          postgres    false    220         �            1259    94468 	   productos    TABLE     �   CREATE TABLE public.productos (
    id integer NOT NULL,
    proveedor_id integer,
    nombre character varying(30),
    precio numeric(13,2),
    existencia integer
);
    DROP TABLE public.productos;
       public         heap    postgres    false         �            1259    94503 
   productos1    TABLE     �   CREATE TABLE public.productos1 (
    id integer NOT NULL,
    proveedor_id integer,
    nombre character varying(30),
    precio numeric(13,2),
    existencia integer
);
    DROP TABLE public.productos1;
       public         heap    postgres    false         �            1259    94502    productos1_id_seq    SEQUENCE     �   CREATE SEQUENCE public.productos1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.productos1_id_seq;
       public          postgres    false    229                    0    0    productos1_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.productos1_id_seq OWNED BY public.productos1.id;
          public          postgres    false    228         �            1259    94467    productos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.productos_id_seq;
       public          postgres    false    225                    0    0    productos_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;
          public          postgres    false    224         �            1259    94441    proveedores    TABLE     �   CREATE TABLE public.proveedores (
    id integer NOT NULL,
    nombre character varying(30),
    direccion text,
    telefono character varying(20),
    correo character varying(60)
);
    DROP TABLE public.proveedores;
       public         heap    postgres    false         �            1259    94492    proveedores1    TABLE     �   CREATE TABLE public.proveedores1 (
    id integer NOT NULL,
    nombre character varying(30),
    direccion text,
    telefono character varying(20),
    correo character varying(60)
);
     DROP TABLE public.proveedores1;
       public         heap    postgres    false         �            1259    94491    proveedores1_id_seq    SEQUENCE     �   CREATE SEQUENCE public.proveedores1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.proveedores1_id_seq;
       public          postgres    false    227                    0    0    proveedores1_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.proveedores1_id_seq OWNED BY public.proveedores1.id;
          public          postgres    false    226         �            1259    94440    proveedores_id_seq    SEQUENCE     �   CREATE SEQUENCE public.proveedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.proveedores_id_seq;
       public          postgres    false    223                    0    0    proveedores_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.proveedores_id_seq OWNED BY public.proveedores.id;
          public          postgres    false    222         �            1259    94593    vista_prov_prod    VIEW     �   CREATE VIEW public.vista_prov_prod AS
 SELECT a.nombre AS proveedor,
    a.telefono,
    a.correo,
    b.nombre AS producto,
    b.precio,
    b.existencia
   FROM public.proveedores a,
    public.productos b
  WHERE (b.proveedor_id = a.id);
 "   DROP VIEW public.vista_prov_prod;
       public          postgres    false    225    223    223    225    225    225    223    223         C           2604    94208    contactos3 id    DEFAULT     n   ALTER TABLE ONLY public.contactos3 ALTER COLUMN id SET DEFAULT nextval('public.contactos3_id_seq'::regclass);
 <   ALTER TABLE public.contactos3 ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219         D           2604    94229    contactos4 id    DEFAULT     n   ALTER TABLE ONLY public.contactos4 ALTER COLUMN id SET DEFAULT nextval('public.contactos4_id_seq'::regclass);
 <   ALTER TABLE public.contactos4 ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221         F           2604    94471    productos id    DEFAULT     l   ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);
 ;   ALTER TABLE public.productos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    225    225         H           2604    94506    productos1 id    DEFAULT     n   ALTER TABLE ONLY public.productos1 ALTER COLUMN id SET DEFAULT nextval('public.productos1_id_seq'::regclass);
 <   ALTER TABLE public.productos1 ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    228    229         E           2604    94444    proveedores id    DEFAULT     p   ALTER TABLE ONLY public.proveedores ALTER COLUMN id SET DEFAULT nextval('public.proveedores_id_seq'::regclass);
 =   ALTER TABLE public.proveedores ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    222    223         G           2604    94495    proveedores1 id    DEFAULT     r   ALTER TABLE ONLY public.proveedores1 ALTER COLUMN id SET DEFAULT nextval('public.proveedores1_id_seq'::regclass);
 >   ALTER TABLE public.proveedores1 ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    226    227         �          0    94105 	   contactos 
   TABLE DATA           Y   COPY public.contactos (nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
    public          postgres    false    215       4851.dat �          0    94174 
   contactos1 
   TABLE DATA           Z   COPY public.contactos1 (nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
    public          postgres    false    216       4852.dat �          0    94194 
   contactos2 
   TABLE DATA           Z   COPY public.contactos2 (nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
    public          postgres    false    217       4853.dat �          0    94205 
   contactos3 
   TABLE DATA           ^   COPY public.contactos3 (id, nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
    public          postgres    false    219       4855.dat �          0    94226 
   contactos4 
   TABLE DATA           ^   COPY public.contactos4 (id, nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
    public          postgres    false    221       4857.dat �          0    94468 	   productos 
   TABLE DATA           Q   COPY public.productos (id, proveedor_id, nombre, precio, existencia) FROM stdin;
    public          postgres    false    225       4861.dat           0    94503 
   productos1 
   TABLE DATA           R   COPY public.productos1 (id, proveedor_id, nombre, precio, existencia) FROM stdin;
    public          postgres    false    229       4865.dat �          0    94441    proveedores 
   TABLE DATA           N   COPY public.proveedores (id, nombre, direccion, telefono, correo) FROM stdin;
    public          postgres    false    223       4859.dat �          0    94492    proveedores1 
   TABLE DATA           O   COPY public.proveedores1 (id, nombre, direccion, telefono, correo) FROM stdin;
    public          postgres    false    227       4863.dat            0    0    contactos3_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.contactos3_id_seq', 4, true);
          public          postgres    false    218                    0    0    contactos4_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.contactos4_id_seq', 3, true);
          public          postgres    false    220                    0    0    productos1_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.productos1_id_seq', 16, true);
          public          postgres    false    228                    0    0    productos_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.productos_id_seq', 16, true);
          public          postgres    false    224                    0    0    proveedores1_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.proveedores1_id_seq', 4, true);
          public          postgres    false    226                    0    0    proveedores_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.proveedores_id_seq', 4, true);
          public          postgres    false    222         N           2606    94210    contactos3 contactos3_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.contactos3
    ADD CONSTRAINT contactos3_pkey PRIMARY KEY (id, cedula, correo);
 D   ALTER TABLE ONLY public.contactos3 DROP CONSTRAINT contactos3_pkey;
       public            postgres    false    219    219    219         P           2606    94253     contactos4 contactos4_cedula_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.contactos4
    ADD CONSTRAINT contactos4_cedula_key UNIQUE (cedula);
 J   ALTER TABLE ONLY public.contactos4 DROP CONSTRAINT contactos4_cedula_key;
       public            postgres    false    221         R           2606    94233     contactos4 contactos4_correo_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.contactos4
    ADD CONSTRAINT contactos4_correo_key UNIQUE (correo);
 J   ALTER TABLE ONLY public.contactos4 DROP CONSTRAINT contactos4_correo_key;
       public            postgres    false    221         T           2606    94231    contactos4 contactos4_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.contactos4
    ADD CONSTRAINT contactos4_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.contactos4 DROP CONSTRAINT contactos4_pkey;
       public            postgres    false    221         `           2606    94508    productos1 productos1_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.productos1
    ADD CONSTRAINT productos1_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.productos1 DROP CONSTRAINT productos1_pkey;
       public            postgres    false    229         Z           2606    94473    productos productos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.productos DROP CONSTRAINT productos_pkey;
       public            postgres    false    225         \           2606    94501 $   proveedores1 proveedores1_correo_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.proveedores1
    ADD CONSTRAINT proveedores1_correo_key UNIQUE (correo);
 N   ALTER TABLE ONLY public.proveedores1 DROP CONSTRAINT proveedores1_correo_key;
       public            postgres    false    227         ^           2606    94499    proveedores1 proveedores1_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.proveedores1
    ADD CONSTRAINT proveedores1_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.proveedores1 DROP CONSTRAINT proveedores1_pkey;
       public            postgres    false    227         V           2606    94450 "   proveedores proveedores_correo_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_correo_key UNIQUE (correo);
 L   ALTER TABLE ONLY public.proveedores DROP CONSTRAINT proveedores_correo_key;
       public            postgres    false    223         X           2606    94448    proveedores proveedores_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.proveedores DROP CONSTRAINT proveedores_pkey;
       public            postgres    false    223         L           2606    94198    contactos2 uniq_ced_cor 
   CONSTRAINT     \   ALTER TABLE ONLY public.contactos2
    ADD CONSTRAINT uniq_ced_cor UNIQUE (cedula, correo);
 A   ALTER TABLE ONLY public.contactos2 DROP CONSTRAINT uniq_ced_cor;
       public            postgres    false    217    217         J           2606    94178    contactos1 uniq_cedula 
   CONSTRAINT     S   ALTER TABLE ONLY public.contactos1
    ADD CONSTRAINT uniq_cedula UNIQUE (cedula);
 @   ALTER TABLE ONLY public.contactos1 DROP CONSTRAINT uniq_cedula;
       public            postgres    false    216         a           2606    94474    productos fk_proveedor_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.productos
    ADD CONSTRAINT fk_proveedor_id FOREIGN KEY (proveedor_id) REFERENCES public.proveedores(id);
 C   ALTER TABLE ONLY public.productos DROP CONSTRAINT fk_proveedor_id;
       public          postgres    false    4696    225    223                    0    0 '   CONSTRAINT fk_proveedor_id ON productos    COMMENT     o   COMMENT ON CONSTRAINT fk_proveedor_id ON public.productos IS 'Este es un ejemplo de asociación entre tablas';
          public          postgres    false    4705         b           2606    94509 '   productos1 productos1_proveedor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.productos1
    ADD CONSTRAINT productos1_proveedor_id_fkey FOREIGN KEY (proveedor_id) REFERENCES public.proveedores1(id) NOT VALID;
 Q   ALTER TABLE ONLY public.productos1 DROP CONSTRAINT productos1_proveedor_id_fkey;
       public          postgres    false    227    229    4702                                                                                         4851.dat                                                                                            0000600 0004000 0002000 00000000005 14775027576 0014272 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4852.dat                                                                                            0000600 0004000 0002000 00000000203 14775027576 0014273 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        ANA	VASQUEZ	1960-08-15	+58 212 9876543	av@gmail.com	V7654321
YOLANDA	TORTOZA	1970-09-25	+58 212 5876543	yt@gmail.com	V9654321
\.


                                                                                                                                                                                                                                                                                                                                                                                             4853.dat                                                                                            0000600 0004000 0002000 00000000203 14775027576 0014274 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        ANA	VASQUEZ	1960-08-15	+58 212 9876543	av@gmail.com	V7654321
YOLANDA	TORTOZA	1970-09-25	+58 212 5876543	yt@gmail.com	V9654321
\.


                                                                                                                                                                                                                                                                                                                                                                                             4855.dat                                                                                            0000600 0004000 0002000 00000000411 14775027576 0014277 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	ANA	VASQUEZ	1960-08-15	+58 212 9876543	av@gmail.com	V7654321
2	YOLANDA	TORTOZA	1970-09-25	+58 212 5876543	yt@gmail.com	V9654321
3	ANA	VASQUEZ	1960-08-15	+58 212 9876543	av@gmail.com	V7654321
4	YOLANDA	TORTOZA	1970-09-25	+58 212 5876543	yt@gmail.com	V9654321
\.


                                                                                                                                                                                                                                                       4857.dat                                                                                            0000600 0004000 0002000 00000000207 14775027576 0014304 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	ANA	VASQUEZ	1960-08-15	+58 212 9876543	av@gmail.com	V7654321
2	YOLANDA	TORTOZA	1970-09-25	+58 212 5876543	yt@gmail.com	V9654321
\.


                                                                                                                                                                                                                                                                                                                                                                                         4861.dat                                                                                            0000600 0004000 0002000 00000000616 14775027576 0014303 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	1	NEVERA	500.25	12
2	1	LAVADORA	300.75	6
3	1	SECADORA	500.50	8
4	1	CONGELADOR	200.25	3
5	2	AIRE ACONDICIONADO	600.00	3
6	2	COCINA ELECTRICA	250.00	6
7	2	COCINA A GAS	175.00	9
8	2	NEVERA	480.00	7
9	3	LAVADORA	500.00	2
10	3	HORNO ELECTRICO	350.00	3
11	3	MICRO ONDAS	150.00	6
12	3	CONGELADOR	250.00	3
13	4	NEVERA	490.00	7
14	4	HORNO A GAS	250.00	6
15	4	SECADORA	550.00	5
16	4	LAVADORA	450.00	6
\.


                                                                                                                  4865.dat                                                                                            0000600 0004000 0002000 00000000616 14775027576 0014307 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	1	NEVERA	500.25	12
2	1	LAVADORA	300.75	6
3	1	SECADORA	500.50	8
4	1	CONGELADOR	200.25	3
5	2	AIRE ACONDICIONADO	600.00	3
6	2	COCINA ELECTRICA	250.00	6
7	2	COCINA A GAS	175.00	9
8	2	NEVERA	480.00	7
9	3	LAVADORA	500.00	2
10	3	HORNO ELECTRICO	350.00	3
11	3	MICRO ONDAS	150.00	6
12	3	CONGELADOR	250.00	3
13	4	NEVERA	490.00	7
14	4	HORNO A GAS	250.00	6
15	4	SECADORA	550.00	5
16	4	LAVADORA	450.00	6
\.


                                                                                                                  4859.dat                                                                                            0000600 0004000 0002000 00000000362 14775027576 0014310 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	GE	AV. LECUNA	+58 212 9876543	info@ge.com
2	LG	AV. ROMULO GALLEGOS	+58 212 8876543	info@lg.com
3	WHIRPOOL	AV. FCO. DE MIRANDA	+58 212 7876543	info@whirpool.com
4	ELECTROLUX	AV. PPAL. DE LAS MERCEDES	+58 212 6876543	info@electrolux.com
\.


                                                                                                                                                                                                                                                                              4863.dat                                                                                            0000600 0004000 0002000 00000000362 14775027576 0014303 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	GE	AV. LECUNA	+58 212 9876543	info@ge.com
2	LG	AV. ROMULO GALLEGOS	+58 212 8876543	info@lg.com
3	WHIRPOOL	AV. FCO. DE MIRANDA	+58 212 7876543	info@whirpool.com
4	ELECTROLUX	AV. PPAL. DE LAS MERCEDES	+58 212 6876543	info@electrolux.com
\.


                                                                                                                                                                                                                                                                              restore.sql                                                                                         0000600 0004000 0002000 00000036256 14775027576 0015424 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE bd_ig_henry;
--
-- Name: bd_ig_henry; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE bd_ig_henry WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Venezuela.1252';


ALTER DATABASE bd_ig_henry OWNER TO postgres;

\connect bd_ig_henry

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: contactos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contactos (
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);


ALTER TABLE public.contactos OWNER TO postgres;

--
-- Name: TABLE contactos; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.contactos IS 'Ejemplo de tabla secuencial';


--
-- Name: contactos1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contactos1 (
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);


ALTER TABLE public.contactos1 OWNER TO postgres;

--
-- Name: TABLE contactos1; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.contactos1 IS 'Tabla con índice único';


--
-- Name: contactos2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contactos2 (
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);


ALTER TABLE public.contactos2 OWNER TO postgres;

--
-- Name: contactos3; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contactos3 (
    id integer NOT NULL,
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60) NOT NULL,
    cedula character varying(15) NOT NULL
);


ALTER TABLE public.contactos3 OWNER TO postgres;

--
-- Name: TABLE contactos3; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.contactos3 IS 'Ejemplo de tabla que contendrá clave primaria para un campo serial, identficado con el nombre id';


--
-- Name: contactos3_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contactos3_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contactos3_id_seq OWNER TO postgres;

--
-- Name: contactos3_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contactos3_id_seq OWNED BY public.contactos3.id;


--
-- Name: contactos4; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contactos4 (
    id bigint NOT NULL,
    nombre character varying(80),
    apellido character varying(80),
    fechanac date,
    telefono character varying(20),
    correo character varying(60),
    cedula character varying(15)
);


ALTER TABLE public.contactos4 OWNER TO postgres;

--
-- Name: contactos4_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contactos4_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contactos4_id_seq OWNER TO postgres;

--
-- Name: contactos4_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contactos4_id_seq OWNED BY public.contactos4.id;


--
-- Name: productos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos (
    id integer NOT NULL,
    proveedor_id integer,
    nombre character varying(30),
    precio numeric(13,2),
    existencia integer
);


ALTER TABLE public.productos OWNER TO postgres;

--
-- Name: productos1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos1 (
    id integer NOT NULL,
    proveedor_id integer,
    nombre character varying(30),
    precio numeric(13,2),
    existencia integer
);


ALTER TABLE public.productos1 OWNER TO postgres;

--
-- Name: productos1_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.productos1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos1_id_seq OWNER TO postgres;

--
-- Name: productos1_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.productos1_id_seq OWNED BY public.productos1.id;


--
-- Name: productos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_id_seq OWNER TO postgres;

--
-- Name: productos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;


--
-- Name: proveedores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proveedores (
    id integer NOT NULL,
    nombre character varying(30),
    direccion text,
    telefono character varying(20),
    correo character varying(60)
);


ALTER TABLE public.proveedores OWNER TO postgres;

--
-- Name: proveedores1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proveedores1 (
    id integer NOT NULL,
    nombre character varying(30),
    direccion text,
    telefono character varying(20),
    correo character varying(60)
);


ALTER TABLE public.proveedores1 OWNER TO postgres;

--
-- Name: proveedores1_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proveedores1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.proveedores1_id_seq OWNER TO postgres;

--
-- Name: proveedores1_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proveedores1_id_seq OWNED BY public.proveedores1.id;


--
-- Name: proveedores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proveedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.proveedores_id_seq OWNER TO postgres;

--
-- Name: proveedores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proveedores_id_seq OWNED BY public.proveedores.id;


--
-- Name: vista_prov_prod; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.vista_prov_prod AS
 SELECT a.nombre AS proveedor,
    a.telefono,
    a.correo,
    b.nombre AS producto,
    b.precio,
    b.existencia
   FROM public.proveedores a,
    public.productos b
  WHERE (b.proveedor_id = a.id);


ALTER VIEW public.vista_prov_prod OWNER TO postgres;

--
-- Name: contactos3 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos3 ALTER COLUMN id SET DEFAULT nextval('public.contactos3_id_seq'::regclass);


--
-- Name: contactos4 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos4 ALTER COLUMN id SET DEFAULT nextval('public.contactos4_id_seq'::regclass);


--
-- Name: productos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);


--
-- Name: productos1 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos1 ALTER COLUMN id SET DEFAULT nextval('public.productos1_id_seq'::regclass);


--
-- Name: proveedores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores ALTER COLUMN id SET DEFAULT nextval('public.proveedores_id_seq'::regclass);


--
-- Name: proveedores1 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores1 ALTER COLUMN id SET DEFAULT nextval('public.proveedores1_id_seq'::regclass);


--
-- Data for Name: contactos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contactos (nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
\.
COPY public.contactos (nombre, apellido, fechanac, telefono, correo, cedula) FROM '$$PATH$$/4851.dat';

--
-- Data for Name: contactos1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contactos1 (nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
\.
COPY public.contactos1 (nombre, apellido, fechanac, telefono, correo, cedula) FROM '$$PATH$$/4852.dat';

--
-- Data for Name: contactos2; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contactos2 (nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
\.
COPY public.contactos2 (nombre, apellido, fechanac, telefono, correo, cedula) FROM '$$PATH$$/4853.dat';

--
-- Data for Name: contactos3; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contactos3 (id, nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
\.
COPY public.contactos3 (id, nombre, apellido, fechanac, telefono, correo, cedula) FROM '$$PATH$$/4855.dat';

--
-- Data for Name: contactos4; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contactos4 (id, nombre, apellido, fechanac, telefono, correo, cedula) FROM stdin;
\.
COPY public.contactos4 (id, nombre, apellido, fechanac, telefono, correo, cedula) FROM '$$PATH$$/4857.dat';

--
-- Data for Name: productos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos (id, proveedor_id, nombre, precio, existencia) FROM stdin;
\.
COPY public.productos (id, proveedor_id, nombre, precio, existencia) FROM '$$PATH$$/4861.dat';

--
-- Data for Name: productos1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos1 (id, proveedor_id, nombre, precio, existencia) FROM stdin;
\.
COPY public.productos1 (id, proveedor_id, nombre, precio, existencia) FROM '$$PATH$$/4865.dat';

--
-- Data for Name: proveedores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.proveedores (id, nombre, direccion, telefono, correo) FROM stdin;
\.
COPY public.proveedores (id, nombre, direccion, telefono, correo) FROM '$$PATH$$/4859.dat';

--
-- Data for Name: proveedores1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.proveedores1 (id, nombre, direccion, telefono, correo) FROM stdin;
\.
COPY public.proveedores1 (id, nombre, direccion, telefono, correo) FROM '$$PATH$$/4863.dat';

--
-- Name: contactos3_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contactos3_id_seq', 4, true);


--
-- Name: contactos4_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contactos4_id_seq', 3, true);


--
-- Name: productos1_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.productos1_id_seq', 16, true);


--
-- Name: productos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.productos_id_seq', 16, true);


--
-- Name: proveedores1_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.proveedores1_id_seq', 4, true);


--
-- Name: proveedores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.proveedores_id_seq', 4, true);


--
-- Name: contactos3 contactos3_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos3
    ADD CONSTRAINT contactos3_pkey PRIMARY KEY (id, cedula, correo);


--
-- Name: contactos4 contactos4_cedula_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos4
    ADD CONSTRAINT contactos4_cedula_key UNIQUE (cedula);


--
-- Name: contactos4 contactos4_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos4
    ADD CONSTRAINT contactos4_correo_key UNIQUE (correo);


--
-- Name: contactos4 contactos4_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos4
    ADD CONSTRAINT contactos4_pkey PRIMARY KEY (id);


--
-- Name: productos1 productos1_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos1
    ADD CONSTRAINT productos1_pkey PRIMARY KEY (id);


--
-- Name: productos productos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);


--
-- Name: proveedores1 proveedores1_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores1
    ADD CONSTRAINT proveedores1_correo_key UNIQUE (correo);


--
-- Name: proveedores1 proveedores1_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores1
    ADD CONSTRAINT proveedores1_pkey PRIMARY KEY (id);


--
-- Name: proveedores proveedores_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_correo_key UNIQUE (correo);


--
-- Name: proveedores proveedores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_pkey PRIMARY KEY (id);


--
-- Name: contactos2 uniq_ced_cor; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos2
    ADD CONSTRAINT uniq_ced_cor UNIQUE (cedula, correo);


--
-- Name: contactos1 uniq_cedula; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactos1
    ADD CONSTRAINT uniq_cedula UNIQUE (cedula);


--
-- Name: productos fk_proveedor_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT fk_proveedor_id FOREIGN KEY (proveedor_id) REFERENCES public.proveedores(id);


--
-- Name: CONSTRAINT fk_proveedor_id ON productos; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON CONSTRAINT fk_proveedor_id ON public.productos IS 'Este es un ejemplo de asociación entre tablas';


--
-- Name: productos1 productos1_proveedor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos1
    ADD CONSTRAINT productos1_proveedor_id_fkey FOREIGN KEY (proveedor_id) REFERENCES public.proveedores1(id) NOT VALID;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  