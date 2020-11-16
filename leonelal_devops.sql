-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: mysql-leonelal.alwaysdata.net
-- Generation Time: Nov 10, 2020 at 01:10 PM
-- Server version: 10.4.12-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `leonelal_devops`
--

-- --------------------------------------------------------

--
-- Table structure for table `automates`
--

CREATE TABLE `automates` (
  `id_automate` int(11) NOT NULL,
  `numero_automate` int(11) DEFAULT NULL,
  `type_automate` varchar(10) DEFAULT NULL,
  `numero_unite` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `automates`
--

INSERT INTO `automates` (`id_automate`, `numero_automate`, `type_automate`, `numero_unite`) VALUES
(1, 1, '0X0000BA20', 1),
(2, 2, '0X0000BA21', 1),
(3, 3, '0X0000BA22', 1),
(4, 4, '0X0000BA23', 1),
(5, 5, '0X0000BA24', 1),
(6, 6, '0X0000BA25', 1),
(7, 7, '0X0000BA26', 1),
(8, 8, '0X0000BA27', 1),
(9, 9, '0X0000BA28', 1),
(10, 10, '0X0000BA29', 1);

-- --------------------------------------------------------

--
-- Table structure for table `donnes`
--

CREATE TABLE `donnes` (
  `id` int(11) NOT NULL,
  `horaire` int(11) DEFAULT NULL,
  `temperature_cuve` float DEFAULT NULL,
  `temperature_exterieure` float DEFAULT NULL,
  `poids_lait_cuve` float DEFAULT NULL,
  `poids_final` float DEFAULT NULL,
  `mesure_pH` float DEFAULT NULL,
  `mesure_Kplus` int(11) DEFAULT NULL,
  `Concentration_NaCI` float DEFAULT NULL,
  `niveau_bacterie_salmonelle` int(11) DEFAULT NULL,
  `niveau_bacterie_Ecoli` int(11) DEFAULT NULL,
  `niveau_bacterie_listeria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `resultats`
--

CREATE TABLE `resultats` (
  `unite` int(11) NOT NULL,
  `machine` int(11) NOT NULL,
  `type_auto` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `unites`
--

CREATE TABLE `unites` (
  `numero_unite` int(11) NOT NULL,
  `nom_unite` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `unites`
--

INSERT INTO `unites` (`numero_unite`, `nom_unite`) VALUES
(1, 'Yaourt'),
(2, 'Fromage'),
(3, 'Beurre'),
(4, 'Lait'),
(5, 'Creme');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `automates`
--
ALTER TABLE `automates`
  ADD PRIMARY KEY (`id_automate`),
  ADD KEY `numero_unite` (`numero_unite`);

--
-- Indexes for table `donnes`
--
ALTER TABLE `donnes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `unites`
--
ALTER TABLE `unites`
  ADD PRIMARY KEY (`numero_unite`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `automates`
--
ALTER TABLE `automates`
  MODIFY `id_automate` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `donnes`
--
ALTER TABLE `donnes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `unites`
--
ALTER TABLE `unites`
  MODIFY `numero_unite` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `automates`
--
ALTER TABLE `automates`
  ADD CONSTRAINT `automates_ibfk_1` FOREIGN KEY (`numero_unite`) REFERENCES `unites` (`numero_unite`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
