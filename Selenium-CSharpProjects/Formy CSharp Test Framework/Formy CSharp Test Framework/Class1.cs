// Default module load upon Class creation
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Modules necessary for C# Framework
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

namespace Formy_CSharp_Test_Framework
{
    public class Chrome_Sample_Test
    {
        private IWebDriver driver;
        public string homeURL;

        [Test(Description ="Check SauceLabs Homepage for Login Link")]
        public void Login_is_on_home_page()
        {
            homeURL = "https://www.SauceLabs.com";
            driver.Navigate().GoToUrl(homeURL);
            WebDriverWait wait = new WebDriverWait(driver, System.TimeSpan.FromSeconds(15));
            wait.Until(driver => driver.FindElement(By.XPath("//*[@id="headerMainNav"]/div/nav/ul/li[3]/ul/li[2]/a")));
        }
     }
}
