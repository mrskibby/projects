-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2020 at 10:47 AM
-- Server version: 10.1.10-MariaDB
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myrent_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bookID` int(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `car` varchar(50) NOT NULL,
  `location` varchar(500) NOT NULL,
  `pickdate` varchar(500) NOT NULL,
  `returndate` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bookID`, `username`, `car`, `location`, `pickdate`, `returndate`) VALUES
(40, '111', 'Axia', 'PickUp Location', '2019-10-15', '2019-10-24'),
(42, '111', 'Alza', 'Skudai', '2019-10-15', '2019-10-18'),
(43, '001', 'Myvi', 'Johor Bahru', '2019-10-15', '2019-10-18'),
(44, 'megatron', 'Myvi', 'Senai', '2012-12-19', '2001-01-20'),
(45, 'megatron', 'Myvi', 'Skudai', '1970-01-01', '1970-01-01'),
(46, 'megatron', 'Myvi', 'Skudai', '1970-01-01', '1970-01-01'),
(47, 'megatron', 'Myvi', 'Senai', '1970-01-01', '1970-01-01'),
(49, 'nsakib123', 'Axia', 'Skudai', '1970-01-01', '1970-01-01'),
(50, 'nsakib123', 'Axia', 'Skudai', '1970-01-01', '1970-01-01'),
(51, 'nsakib123', 'Axia', 'Skudai', '2019-12-25', '2019-12-26'),
(52, 'nsakib123', 'Axia', 'Skudai', '2019-12-25', '2019-12-27');

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

CREATE TABLE `cars` (
  `carname` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Rent` int(50) NOT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`carname`, `Type`, `Rent`, `ID`) VALUES
('Axia', '4 Seater', 100, 0);

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `drivername` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`drivername`, `Type`, `ID`) VALUES
('Sakib', 'Half Time', 1122);

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `id` int(11) NOT NULL,
  `lat` float(10,6) NOT NULL,
  `lng` float(10,6) NOT NULL,
  `name` varchar(200) NOT NULL,
  `location_status` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`id`, `lat`, `lng`, `name`, `location_status`) VALUES
(2, 1.861076, 102.938553, 'Miraj Ahmed', 1),
(3, 1.556662, 103.818596, 'Sakib', 1),
(4, 1.538871, 103.664497, 'Dip', 1);

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `Fullname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pnum` int(20) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `mess` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`Fullname`, `email`, `pnum`, `subject`, `mess`) VALUES
('', '', 0, '', ''),
('aef', 'eaf@gmail.com', 0, 'afaef', 'hi welcome'),
('sfbs', 'sgs@gmail.com', 0, 'sggs', 'sdsgd'),
('aaf', 'thar@gmail.com', 1231, 'eefsvsrvr', 'hola'),
('jyrfyud', 'uyrfuyf@tty', 12345, 'jg', 'jhgjhf');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Firstname` varchar(50) NOT NULL,
  `Lastname` varchar(50) NOT NULL,
  `pnum` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `link` varchar(1000) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `Admin` int(11) NOT NULL DEFAULT '1',
  `verified` int(2) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Firstname`, `Lastname`, `pnum`, `Email`, `link`, `username`, `password`, `Admin`, `verified`) VALUES
('RAHAT ', 'ABI', '215416524', '', '', '110', '1234', 0, 1),
('dip', 'joti', '123456', 'dip@dip.com', '', 'dip23', 'dip23', 0, 1),
('mega', 'tron', '1234567', 'mega@tron.com', 'https://drive.google.com/open?id=0Byn1DahAsJmOLU9vSlQ3U3dVQmhYSzI0cU5CeDdwNHpoWFNF', 'megatron', '1122', 0, 1),
('akib', 'DIP', '23242', 'akib@dip.com', '', 'miraj', '22446688', 1, 0),
('Nazmus', 'sakib', '01156398909', 'nsakib360@gmail.com', '', 'nsakib123', 'sakib123', 0, 1),
('nazmus', 'sakib', '1234567', 'sakib330@gmail.com', '', 'nskibby', '1234567', 0, 1),
('reza', 'erabby', '372352835', 'rezaerabbysakib015@gmail.com', '', 'reza', '22446688', 0, 0),
('yo', 'yo', '0000000', 'yo@gmail.com', '', 'yo', '12345', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bookID`);

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bookID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;
--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
