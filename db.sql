CREATE TABLE `measures` (
  `id` int(10) UNSIGNED NOT NULL,
  `unitNumber` int(11) NOT NULL,
  `robotNumber` int(11) NOT NULL,
  `robotType` varchar(255) NOT NULL,
  `tankTemp` double(8,2) NOT NULL,
  `extTemp` double(8,2) NOT NULL,
  `tankWeight` double(8,2) NOT NULL,
  `productWeight` double(8,2) NOT NULL,
  `ph` double(8,2) NOT NULL,
  `kPlus` int(11) NOT NULL,
  `nacl` double(8,2) NOT NULL,
  `salmonellaLevel` int(11) NOT NULL,
  `ecoliLevel` int(11) NOT NULL,
  `listeriaLevel` int(11) NOT NULL,
  `timeStamp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `measures`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `measures`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;