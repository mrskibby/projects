

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";




--Created By Brothers from another mother.
--
--
-- Database: `utm_space_booking`
--
--
-- --------------------------------------------------------
--
--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin@gmail.com', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `create_account`
--

CREATE TABLE `create_account` (
  `id` int(11) NOT NULL,
  `name` char(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `gender` enum('male','female','other') NOT NULL,
  `country` varchar(50) NOT NULL,
  `pictrure` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `create_account`
--

INSERT INTO `create_account` (`id`, `name`, `email`, `password`, `mobile`, `address`, `gender`, `country`, `pictrure`) VALUES
(4, 'Nazmus Sakib', 'nsakib360@gmail.com', '1234', 012345, 'UTM KDOJ', 'male', 'Bangladesh', ''),
(7, 'Miraj Ahmed', 'Miraj@gmail.com', '1234', 012345, 'UTM KTHO', 'male', 'Bangladesh', ''),
(8, 'Karimul Hasan', 'karimul@gmail.com', '1234', 012345, 'UTM K10', 'male', 'Bangladesh', ''),
(9, 'Nik Adam', 'adam@gmail.com', '1234', 012345, 'UTM KTDI', 'male', 'Malaysia', ''),
(10, 'Megan Rahman', 'megan@gmail.com', '1234', 012345, 'UTM KDOJ', 'male', 'Bangladesh', ''),
(11, 'Rahat Shariar', 'rahat@gmail.com', '1234', 012345, 'UTM KDOJ', 'male', 'Bangladesh', ''),
(12, 'Jack Ma', 'jack@gmail.com', '1234', 012345, 'Noida', 'male', 'China', '');

-- --------------------------------------------------------

--
-- Table structure for table `details_slider`
--

CREATE TABLE `details_slider` (
  `id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  `caption` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `message` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `name`, `email`, `mobile`, `message`) VALUES
(1, 'Nazmus', 'nsakib360@gmail.com', 012345, 'Nice');

-- --------------------------------------------------------

--
-- Table structure for table `halls`
--

CREATE TABLE `halls` (
  `hall_id` int(11) NOT NULL,
  `hall_no` int(11) NOT NULL,
  `type` varchar(100) NOT NULL,
  `price` bigint(20) NOT NULL,
  `details` text NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `halls`
--

INSERT INTO `halls` (`hall_id`, `hall_no`, `type`, `price`, `details`, `image`) VALUES
(28, 01, 'Dewan Sri Perdana', 150, 'Perdana is really famous for Wedding Ceremony. Most of the wedding ceremonies inside UTM is held in Dewan Sri Perdana. It has space for almost 200 people.', ''),
(30, 03, 'DSI', 200, 'An exclusive and biggest hall in UTM. Can book for really big events and cultural shows. Has ample space and a big stage with lighting facilities.', ''),
(31, 02, 'Dewan Sri Merbau', 100, 'A Spacious Hall suitable for gatherings, meetings and rehearsals.', ''),
(32, 05, 'Dewan Sri Meranti', 50, 'A Spacious Hall suitable for gatherings, meetings and rehearsals.', ''),
(33, 04, 'Dewan Banquet Hall', 80, 'Spacious and suitable for Buffet Arrangement.', ''),
(34, 06, 'Shop Lot', 30, 'Cheap and spacious. Can accomodate lot of shops.', '');

-- --------------------------------------------------------

--
-- Table structure for table `Hall_booking_details`
--

CREATE TABLE `hall_booking_details` (
  `id` int(11) NOT NULL,
  `name` char(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `zip` int(20) NOT NULL,
  `country` varchar(50) NOT NULL,
  `hall_type` varchar(100) NOT NULL,
  `check_in_date` date NOT NULL,
  `check_in_time` varchar(6) NOT NULL,
  `check_out_date` date NOT NULL,
  `Occupancy` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `hall_booking_details`
--

INSERT INTO `hall_booking_details` (`id`, `name`, `email`, `phone`, `address`, `city`, `state`, `zip`, `country`, `hall_type`, `check_in_date`, `check_in_time`, `check_out_date`, `Occupancy`) VALUES
(5, 'Nazmus Sakib', 'nsakib360@gmail.com', 012345, 'UTM KDOJ', 'Skudai', 'Johor', 81310, 'Bangladesh', 'Dewan Sri Perdana', '2019-12-05', '12:00', '2019-01-06', 'Full day'),
(6, 'Miraj', 'Miraj@gmail.com', 012345, 'UTM KTHO', 'Skudai', 'Johor',81310, 'Bangladesh', 'Dewan Sri Perdana', '2019-05-08', '08:00', '2019-06-04', 'Half day'),
(7, 'Nik Adam', 'adam@gmail.com', 012345, 'UTM KTDI', 'Skudai', 'Johor', 81310, 'Malaysia', 'Dewan Sri Merbau', '2019-12-06', '08:00', '2019-12-06', 'Half day'),
(8, 'Karimul Hasan', 'karimul@gmail.com', 012345, 'UTM K10', 'Skudai', 'Johor', 81310, 'Bangladesh', 'Dewan Sri Merbau', '2019-12-06', '08:00', '2019-12-06', 'Full day'),
(12, 'Megan', 'megan@gmail.com', 012345, 'UTM KDOJ', 'Skudai', 'Johor', 81310, 'Bangladesh', 'Dewan Sri Meranti', '2019-05-22', '22:57', '2017-10-31', 'Half day');

-- --------------------------------------------------------

--
-- Table structure for table `slider`
--

CREATE TABLE `slider` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `caption` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `slider`
--

INSERT INTO `slider` (`id`, `image`, `caption`) VALUES
(3, 'img3.jpg', ''),
(6, 'img2.jpg', ''),
(8, 'img1.png', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `create_account`
--
ALTER TABLE `create_account`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `details_slider`
--
ALTER TABLE `details_slider`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `halls`
--
ALTER TABLE `halls`
  ADD PRIMARY KEY (`hall_id`);

--
-- Indexes for table `hall_booking_details`
--
ALTER TABLE `hall_booking_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `slider`
--
ALTER TABLE `slider`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `create_account`
--
ALTER TABLE `create_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `details_slider`
--
ALTER TABLE `details_slider`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `halls`
--
ALTER TABLE `halls`
  MODIFY `hall_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT for table `hall_booking_details`
--
ALTER TABLE `hall_booking_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `slider`
--
ALTER TABLE `slider`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
