-- Create the "user" table
CREATE TABLE "user" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),  -- UUID as primary key
    username VARCHAR(120) UNIQUE NOT NULL,          -- Unique username
    password VARCHAR(255) NOT NULL,                 -- Hashed password
    email VARCHAR(255) UNIQUE NOT NULL,             -- Unique email
    surname VARCHAR(120),                           -- Optional surname
    firstname VARCHAR(120),                         -- Optional firstname
    description TEXT,                               -- Optional description
    created_at TIMESTAMP NOT NULL,    -- Timestamp when created
    updated_at TIMESTAMP,             -- Auto-updated timestamp for changes
    CONSTRAINT user_unique_email UNIQUE (email)     -- Email uniqueness constraint
);

-- Create the "role" table
CREATE TABLE "role" (
    id SERIAL PRIMARY KEY,                          -- Auto-incrementing primary key
    name VARCHAR(100) UNIQUE NOT NULL                -- Unique role name
);

-- Create the "user_roles" table (association table for User and Role)
CREATE TABLE "user_role" (
    id SERIAL PRIMARY KEY,                          -- Auto-incrementing primary key
    user_id UUID NOT NULL,                          -- User foreign key
    role_id INT NOT NULL,                           -- Role foreign key
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES "user" (id) ON DELETE CASCADE,
    CONSTRAINT fk_role FOREIGN KEY (role_id) REFERENCES "role" (id) ON DELETE CASCADE
);

-- Create the "access_token" table
CREATE TABLE "access_token" (
    id SERIAL PRIMARY KEY,                          -- Auto-incrementing primary key
    user_id UUID NOT NULL,                          -- Foreign key to the user table
    token VARCHAR(512) NOT NULL,                    -- Access token
    refresh_token VARCHAR(512),                    -- Refresh token
    created_at TIMESTAMP NOT NULL,    -- Timestamp when created
    expires_at TIMESTAMP NOT NULL,                 -- Token expiration timestamp
    revoked BOOLEAN NOT NULL DEFAULT FALSE,        -- Indicates if the token is revoked
    ip_address VARCHAR(45),                        -- Optional: IP address
    device_info TEXT,                               -- Optional: Device information
    updated_at TIMESTAMP, 
    CONSTRAINT fk_user_access FOREIGN KEY (user_id) REFERENCES "user" (id) ON DELETE CASCADE
);

CREATE TABLE "email_verification" (
    id SERIAL PRIMARY KEY,                           -- Auto-incrementing unique ID
    user_id UUID NOT NULL,                           -- User ID (Foreign key to the user table)
    code VARCHAR(10) NOT NULL,                       -- Verification code (can be alphanumeric)
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),     -- Timestamp when the code was created
    expires_at TIMESTAMP NOT NULL,                   -- Expiration time for the code
    verified BOOLEAN NOT NULL DEFAULT FALSE,         -- Status to track if the code has been verified
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES "user" (id) ON DELETE CASCADE
);
