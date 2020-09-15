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
        IWebDriver _driver;

        [SetUp]
        public void SetUp()
        {
            _driver = new ChromeDriver();
            _driver.Navigate().GoToUrl("https://dev.to/jessicabetts");
        }

        [TearDown]
        public void TearDown()
        {
            _driver.Quit();
        }

        public bool IsCorrectUrl(string expectedUrl)
        {
            Thread.Sleep(5000);
            string url = _driver.Url;
            return url == expectedUrl;
        }

        [Test]
        public void SearchForKeywords()
        {
            // Declare Element Locator Variables
            IWebElement searchBar = _driver.FindElement(By.Id("nav-search"));                       // Find Element via Id value
                                                                                                    //IWebElement searchBar = _driver.FindElement(By.Id("navigation"));                     // Find Element via non-valid Id value to cause exception
                                                                                                    //IWebElement searchBar = _driver.FindElement(By.XPath("//*[@id='nav - search']"));     // Find Element via Xpath value

            // Test Actions
            searchBar.SendKeys("google maps api react");                                            // Type the String into the Search Bar
            searchBar.SendKeys(Keys.Enter);                                                         // Submits the values

            // Declare Test Variables
            string expectedUrl = "https://dev.to/search?q=google%20maps%20api%20react";

            // Verify the Actual URL matches the Expected URL
            Assert.AreEqual(true, IsCorrectUrl(expectedUrl), "The actual URL does not match the expected URL");

        }

        [Test]
        public void NavToHome()
        {
            // Declare Element Locator Variables
            IWebElement logoIcon = _driver.FindElement(By.Id("logo-link"));                         // Find Element via Id value

            // Test Actions
            logoIcon.Click();                                                                        // Click the Logo Icon

            // Declare Test Variables
            string expectedUrl = "https://dev.to/";

            // Verify the Actual URL matches the Expected URL
            Assert.AreEqual(true, IsCorrectUrl(expectedUrl), "The actual URL does not match the expected URL");

        }
    }
}
