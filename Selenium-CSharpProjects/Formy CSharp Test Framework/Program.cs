using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Formy_CSharp_Test_Framework
{
    class Program
    {
        static void Main(string[] args)
        {
            IWebDriver _driver = new ChromeDriver();    // Initialize the driver
            try
            {
                _driver.Navigate().GoToUrl("https://www.dev.to");    // Open the browser to the specified URL
                //IWebElement searchBar = _driver.FindElement(By.Id("nav-search"));   // Find Element via Id value
                IWebElement searchBar = _driver.FindElement(By.Id("navigation"));   // Find Element via non-valid Id value to cause exception
                //IWebElement searchBar = _driver.FindElement(By.XPath("//*[@id='nav - search']"));   // Find Element via Xpath value
                searchBar.SendKeys("google maps api react");        // Type the String into the Search Bar
                searchBar.SendKeys(Keys.Enter);     // Submits the values

                IWebElement latestBtn = _driver.FindElement(By.LinkText("LATEST"));   // Find Element by href text svalue
                latestBtn.Click();  // Clicks the button


                // _driver.Quit();  //Close the browser
                _driver.Close();    //Close the browser
            }
            catch(NoSuchElementException ex)
            {

                Console.WriteLine("The element didn't exist!");
                _driver.Close();    //Close the browser
            }
            
        }
    }
}
