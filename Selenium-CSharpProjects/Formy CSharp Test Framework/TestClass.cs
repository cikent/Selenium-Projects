using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using System;
using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Formy_CSharp_Test_Framework
{
    [TestFixture]
    public class TestClass
    {
        [Test]
        public void Test1()
        {
            // Initialize the driver
            IWebDriver _driver = new ChromeDriver();
            // Open the browser to the specified URL
            _driver.Navigate().GoToUrl("https://www.dev.to");

            // Find Element via Id value
            IWebElement searchBar = _driver.FindElement(By.Id("nav-search"));   
            //IWebElement searchBar = _driver.FindElement(By.Id("navigation"));                     // Find Element via non-valid Id value to cause exception
            //IWebElement searchBar = _driver.FindElement(By.XPath("//*[@id='nav - search']"));     // Find Element via Xpath value
            searchBar.SendKeys("google maps api react");                                            // Type the String into the Search Bar
            searchBar.SendKeys(Keys.Enter);                                                         // Submits the values

            //Thread Sleep, give Results page time to load
            Thread.Sleep(5000);

            //Declare Test Variables
            string actualUrl = _driver.Url;
            string expectedUrl = "https://dev.to/search?q=google%20maps%20api%20react";

            // Verify the Actual URL matches the Expected URL
            Assert.AreEqual(actualUrl, expectedUrl, "The actual URL does not match the expected URL");
            _driver.Quit();

        }

    }
}
