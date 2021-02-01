CREATE TABLE uuser(
    id uuid primary key not null,
    gender char(1) null,
    yearly_income bigint null,
    longitude float null,
    latitude float null
);

CREATE TABLE user_interest(
    id serial primary key,
    user_id uuid not null references uuser,
    interest varchar(50) not null
);

CREATE TABLE advert(
    id uuid primary key not null,
    height int null,
    width int null,
    main_color varchar(20) null
);

CREATE TABLE advert_text(
    id serial primary key,
    advert_id uuid not null references advert,
    text_content text not null
);

CREATE TABLE advert_display(
    id serial primary key,
    user_id uuid not null references uuser,
    advert_id uuid not null references advert,
    display_time timestamp null
);

INSERT INTO uuser
VALUES
  ('01aa0956-1afc-4e97-9df6-487f95a190d6', 'M', 123, 60, 60.1),
  ('7fc99b4c-a51c-4f73-8362-a3d8c9638416', 'M', 12123, 60.2, 60.3),
  ('e3bf931e-07db-4ddf-aaf0-c3e8586e0322', 'F', 1238888, 50.321, 60.1);

INSERT INTO user_interest
VALUES
  (1, '01aa0956-1afc-4e97-9df6-487f95a190d6', 'cyberpunk');

INSERT INTO advert
VALUES
  ('01aa0956-1afc-4e97-9df6-487f95a190d6', 10, 21, '#A03F2A'),
  ('7fc99b4c-a51c-4f73-8362-a3d8c9638416', 11, 20, '#957F7A'),
  ('e3bf931e-07db-4ddf-aaf0-c3e8586e0322', 12, 1238888, '#7A8E95');

INSERT INTO advert_text
VALUES
  (1, '01aa0956-1afc-4e97-9df6-487f95a190d6', 'aaa'),
  (2, '7fc99b4c-a51c-4f73-8362-a3d8c9638416', 'ccc'),
  (3, 'e3bf931e-07db-4ddf-aaf0-c3e8586e0322', 'xxx');

INSERT INTO advert_display
VALUES
  (1, '01aa0956-1afc-4e97-9df6-487f95a190d6', '7fc99b4c-a51c-4f73-8362-a3d8c9638416', '2006-01-02T16:04:05'),
  (2, '7fc99b4c-a51c-4f73-8362-a3d8c9638416', '7fc99b4c-a51c-4f73-8362-a3d8c9638416', '2006-02-02T16:04:05'),
  (3, 'e3bf931e-07db-4ddf-aaf0-c3e8586e0322', 'e3bf931e-07db-4ddf-aaf0-c3e8586e0322', '2006-03-02T16:04:05');