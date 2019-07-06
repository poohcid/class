<?php
/**
 * The header for our theme
 *
 * This is the template that displays all of the <head> section and everything up until <div id="content">
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package Jabont_Simple
 */

?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="profile" href="https://gmpg.org/xfn/11">

	<?php wp_head(); ?>
</head>

<body <?php body_class(); ?> id="newsb">
    <div class="menubar">
       <div class="container">
           <div class="logo">
               <h1>Thai Conscription</h1>
           </div>
           <ul class="menu">
               <li>
                   <a class="change" href="http://161.246.38.35/~it61070166/wordpress/home/">Home</a>
               </li>
               <li>
                   <a class="change" href="about.html">About</a>
               </li>
           </ul>
       </div>
   </div>
</body>