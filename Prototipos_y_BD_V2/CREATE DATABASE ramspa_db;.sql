-- ==========================================
-- 0. CREACIÓN Y SELECCIÓN DE LA BASE DE DATOS
-- ==========================================
CREATE DATABASE IF NOT EXISTS ramspa_db;
USE ramspa_db;

-- ==========================================
-- 1. CREACIÓN DE ESTRUCTURAS (TABLAS)
-- ==========================================

-- Tabla CLIENTES
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    fecha_registro DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS negocios (
    id_negocio INT AUTO_INCREMENT PRIMARY KEY,
    rut_empresa VARCHAR(12) UNIQUE NOT NULL,
    razon_social VARCHAR(150) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS servicios (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio_base DECIMAL(10,2) NOT NULL,
    estado_activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    stock INT DEFAULT 0,
    precio_unitario DECIMAL(10,2) NOT NULL,
    id_proveedor INT
);


INSERT IGNORE INTO clientes (nombre, apellido, email, telefono, fecha_registro) VALUES
('Carlos', 'Soto', 'csoto@email.com', '+56912345678', '2026-09-10'),
('Andrea', 'Gómez', 'agomez@email.com', '+56987654321', '2026-09-12'),
('Luis', 'Pérez', 'lperez@email.com', '+56911223344', '2026-09-15');

INSERT IGNORE INTO negocios (rut_empresa, razon_social, direccion, id_cliente) VALUES
('76.543.210-K', 'Inmobiliaria Centro SPA', 'Av. Providencia 1234, Santiago', 1),
('77.123.456-7', 'Constructora Norte SA', 'Calle Las Industrias 567, Maipú', 3);

INSERT IGNORE INTO servicios (nombre_servicio, descripcion, precio_base, estado_activo) VALUES
('Pulido de Piso Flotante', 'Pulido y vitrificado de pisos flotantes interiores', 45000.00, TRUE),
('Instalación de Cerámica', 'Instalación de cerámicas y porcelanatos por metro cuadrado', 12000.00, TRUE),
('Limpieza Post-Obra', 'Aseo profundo industrial tras término de construcción', 85000.00, TRUE);

INSERT IGNORE INTO productos (nombre_producto, stock, precio_unitario) VALUES
('Cera Acrílica Alto Tráfico 5L', 20, 25000.00),
('Disco de Pulido Diamantado', 15, 35000.00),
('Adhesivo Cerámico Bekron 25kg', 50, 8500.00);

