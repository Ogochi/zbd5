CREATE TABLE uuser(
    id uuid primary key not null,
    gender char(1) null,
    yearly_income bigint null,
    longitude float null,
    latitude float null
);

CREATE TABLE user_interests(
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
    advert_id uuid not null references advert,
    text_content text not null
);

CREATE TABLE advert_display(
    user_id uuid not null references uuser,
    advert_id uuid not null references advert,
    display_time timestamp null
);