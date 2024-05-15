CREATE TABLE labels_label (
    id            bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name          VARCHAR(100),
    created_at    DATE
);

CREATE TABLE statuses_status (
    id            bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name          VARCHAR(100),
    created_at    DATE
);

CREATE TABLE tasks_task (
    id            bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name          VARCHAR(150),
    description   text,
    created_at    DATE
    author_id     bigint REFERENCES users_user (id),
    executor_id   bigint REFERENCES users_user (id),
    status_id     bigint REFERENCES statuses_status (id)
);

CREATE TABLE tasks_task_labels (
    id            bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    task_id       bigint,
    label_id      bigint
);

CREATE TABLE users_user (
    id            bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    password      VARCHAR(128),
    last_login    DATE,
    is_superuser  boolean,
    username      VARCHAR(150),
    first_name    VARCHAR(150),
    last_name     VARCHAR(150),
    email         VARCHAR(254),
    is_staff      boolean,
    is_active     boolean,
    date_joined   DATE
);