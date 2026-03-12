-- creating options

CREATE TYPE occupancy_type_enum AS ENUM (
    'residential',
    'commercial',
    'industrial'
);

CREATE TYPE system_type_enum AS ENUM (
    'wet',
    'dry',
    'pre_action',
    'deluge'
);

CREATE TYPE inspection_type_enum AS ENUM (
    'annual',
    'quarterly',
    'special'
);

CREATE TYPE overall_status_enum AS ENUM (
    'pass',
    'fail',
    'conditional'
);

CREATE TYPE component_type_enum AS ENUM (
    'pipe',
    'sprinkler_head',
    'valve',
    'pump'
);

CREATE TYPE material_enum AS ENUM (
    'steel',
    'cpvc',
    'cast_iron'
);

CREATE TYPE severity_level_enum AS ENUM (
    'low',
    'medium',
    'high',
    'critical'
);


-- Creating tables

CREATE TABLE buildings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    county VARCHAR(100),
    zip_code VARCHAR(20),
    occupancy_type occupancy_type_enum NOT NULL,
    construction_year INT CHECK (construction_year > 1800),
    square_footage INT CHECK (square_footage > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fire_systems (
    id SERIAL PRIMARY KEY,
    building_id INT NOT NULL REFERENCES buildings(id) ON DELETE CASCADE,
    system_type system_type_enum NOT NULL,
    install_date DATE NOT NULL,
    last_major_maintenance_date DATE,
    design_pressure NUMERIC(6,2),
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE components (
    id SERIAL PRIMARY KEY,
    system_id INT NOT NULL REFERENCES fire_systems(id) ON DELETE CASCADE,
    component_type component_type_enum NOT NULL,
    manufacturer VARCHAR(255),
    model VARCHAR(255),
    material material_enum,
    install_date DATE,
    location_description TEXT,
    criticality_level INT CHECK (criticality_level BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE inspections (
    id SERIAL PRIMARY KEY,
    building_id INT NOT NULL REFERENCES buildings(id) ON DELETE CASCADE,
    inspection_date DATE NOT NULL,
    inspection_type inspection_type_enum NOT NULL,
    inspector_name VARCHAR(255),
    overall_status overall_status_enum,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE inspection_results (
    id SERIAL PRIMARY KEY,
    inspection_id INT NOT NULL REFERENCES inspections(id) ON DELETE CASCADE,
    component_id INT NOT NULL REFERENCES components(id) ON DELETE CASCADE,
    condition_score INT CHECK (condition_score BETWEEN 0 AND 100),
    pressure_reading NUMERIC(8,2),
    flow_rate NUMERIC(8,2),
    corrosion_index INT CHECK (corrosion_index BETWEEN 0 AND 10),
    pass_fail BOOLEAN,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE deficiencies (
    id SERIAL PRIMARY KEY,
    inspection_result_id INT NOT NULL REFERENCES inspection_results(id) ON DELETE CASCADE,
    deficiency_code VARCHAR(100),
    severity_level severity_level_enum NOT NULL,
    description TEXT,
    is_recurring BOOLEAN DEFAULT FALSE,
    resolved_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- indexes

CREATE INDEX idx_fire_systems_building ON fire_systems(building_id);
CREATE INDEX idx_components_system ON components(system_id);
CREATE INDEX idx_inspections_building ON inspections(building_id);
CREATE INDEX idx_inspection_results_component ON inspection_results(component_id);
CREATE INDEX idx_inspection_results_inspection ON inspection_results(inspection_id);
CREATE INDEX idx_deficiencies_severity ON deficiencies(severity_level);
CREATE INDEX idx_inspections_date ON inspections(inspection_date);