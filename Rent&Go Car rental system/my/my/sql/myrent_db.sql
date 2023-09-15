-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2019 at 05:02 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
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
(24, '001', 'Axia', 'Tampoi', '2019-08-01', '2019-08-01'),
(27, 'jaanu', 'Myvi', 'Johor Bahru', '2019-07-26', '2019-07-26'),
(31, '110', 'Axia', 'Skudai', '07/31/2019', '08/01/2019'),
(32, '111', 'Alza', 'Johor Bahru', '08/02/2019', '08/03/2019'),
(33, '111', 'Myvi', 'Senai', '2019-08-01', '2019-08-02');

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
('aef', 'eaf@gmail.com', 0, 'afaef', 'hi welcome'),
('aaf', 'thar@gmail.com', 1231, 'eefsvsrvr', 'hola');

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
('MUHAMMAD', 'Jasim', '122334', 'jasim@gmail.com', '', '', '', 0, 0),
('Murthy', 'Tharini', '0182234', 'jjj', '', '001', '1234', 0, 1),
('RAHAT ', 'ABI', '215416524', '', '', '110', '1234', 0, 1),
('Muhammad ', 'Jasim', '', '', '', '111', '1234', 1, 1),
('MUHAMMAD', 'JASIM', '0123456789', 'jasim@gmail.com', 'http://www.google.com', '12345', '1234', 0, 1),
('Tharini', 'Murthy', '0123456789', '', 'https://www.youtube.com/', 'jaanu', '1234', 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bookID`);

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
  MODIFY `bookID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
