CREATE TABLE "offer" (
  "id" uuid PRIMARY KEY,
  "title" varchar(255),
  "price" float,
  "details" json,
  "record_time" date
);

CREATE TABLE "history" (
  "id" uuid PRIMARY KEY,
  "offer_id" uuid,
  "prices" float[],
  "record_times" date[]
);

ALTER TABLE "history" ADD FOREIGN KEY ("offer_id") REFERENCES "offer" ("id");
