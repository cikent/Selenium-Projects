using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.IE;
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
    [TestFixture("Chrome")]
    [TestFixture("Firefox")]
    [TestFixture("IE")]
    [TestFixture]
    public class DriverClass
    {
        IWebDriver _driver;
        string browser;

        //Contstructor for Test Class that takes in which type of browser to use
        public DriverClass(string browserType)
        {
            browser = browserType;
        }

        [SetUp]
        public void Setup()
        {
            if (browser == "Chrome")
            {
                _driver = new ChromeDriver();
            }
            else if (browser == "Firefox")
            {
                _driver = new FirefoxDriver();
            }
            else if (browser == "IE")
            {
                _driver = new InternetExplorerDriver();
            }
        }

        [Test]
        public void ChromeTest()
        {
            IWebDriver _driver = new ChromeDriver();
            _driver.Navigate().GoToUrl("https://dev.to/jessicabetts");

            _driver.Quit();
        }

        [Test]
        public void FirefoxTest()
        {
            IWebDriver _driver = new FirefoxDriver();
            _driver.Navigate().GoToUrl("https://dev.to/jessicabetts");

            _driver.Quit();
        }

        [Test]
        public void IETest()
        {
            IWebDriver _driver = new InternetExplorerDriver();
            _driver.Navigate().GoToUrl("https://dev.to/jessicabetts");

            _driver.Quit();
        }
    }
}
