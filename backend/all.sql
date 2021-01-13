BEGIN TRANSACTION;

INSERT INTO "contracts_currency" ("id","name","code","created","updated","user_id") VALUES (1,'EUR','02','2021-01-12 10:01:04.973841','2021-01-12 10:01:04.973841',1),
 (2,'RON','01','2021-01-12 10:01:14.303649','2021-01-12 10:01:14.303649',1);
INSERT INTO "contracts_vat" ("id","name","code","percent","created","updated","user_id") VALUES (1,'VAT 19','VAT 19',19,'2021-01-12 09:55:58.959655','2021-01-12 09:55:58.959655',1),
 (2,'VAT 21','VAT 21',21,'2021-01-12 09:56:14.979474','2021-01-12 09:56:14.979474',1);
INSERT INTO "contracts_measuringunit" ("id","name","code","created","updated","user_id") VALUES (1,'Time','01','2021-01-12 09:58:09.565213','2021-01-12 09:58:09.565213',1),
 (2,'unit','02','2021-01-12 09:58:31.845354','2021-01-12 09:58:31.845354',1);
INSERT INTO "contracts_itemtype" ("id","name","code","created","updated","user_id") VALUES (1,'Services','01','2021-01-12 09:58:59.047275','2021-01-12 09:58:59.047275',1),
 (2,'Stockable','02','2021-01-12 09:59:27.025347','2021-01-12 09:59:27.025347',1);
INSERT INTO "contracts_contractdetail" ("id","qtty","price","created","updated","item_id_id","user_id","value","contract_id_id") VALUES (1,1,220,'2021-01-12 10:05:49.185098','2021-01-12 10:05:49.185098',1,1,220,1);
INSERT INTO "contracts_item" ("id","name","code","created","updated","item_type_id_id","user_id","vat_id_id","measuring_unit_id_id") VALUES (1,'Item1','01','2021-01-12 09:59:49.740793','2021-01-12 09:59:49.740793',1,1,1,1),
 (2,'Item2','02','2021-01-12 10:00:04.981840','2021-01-12 10:00:04.981840',2,1,2,2);
INSERT INTO "contracts_state" ("id","name","code") VALUES (1,'Valid','01'),
 (2,'Disabled','02'),
 (3,'Inactive','03');
INSERT INTO "contracts_partner" ("id","name","code","fiscal_registration","type","unique_id","created","updated","state_id_id","user_id") VALUES (1,'Partner1','01','213123131232','213123131232',33,'2021-01-12 09:57:23.363183','2021-01-12 09:57:23.363183',1,1),
 (2,'Partner2','02','444444','23432333',234,'2021-01-12 09:57:50.947718','2021-01-12 09:57:50.947718',2,1);
INSERT INTO "contracts_contract" ("id","number","code","start_date","end_date","approved_date","currency_id_id","partner_address_id","notes","dimm_1","dimm_2","dimm_3","dimm_4","category_id","self_partner_id","status_id","responsible_id","repartization_key","renewel_type_id","renewel_end_date","penalty_percent_day","created","updated","user_id","attachment","partner_id_id") VALUES (1,'Ctr 01','01','2021-01-01','2021-01-31','2021-01-01',1,2,'Rent Services',1,23,3,443,1,1,1,1,'21333123',1,'2021-01-01 10:02:36',1,'2021-01-12 10:02:42.456400','2021-01-12 10:02:42.456400',1,'',1);

COMMIT;
