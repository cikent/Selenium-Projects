import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Form {
    public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "C:\\Users\\Inciter\\Code\\Selenium Resources\\Selenium Drivers\\chromedriver.exe");

        WebDriver driver = new ChromeDriver();

        driver.get("https://formy-project.herokuapp.com/form");

        driver.findElement(By.id("first-name")).sendKeys("Chris");

        driver.findElement(By.id("last-name")).sendKeys("Kent");

        driver.findElement(By.id("job-title")).sendKeys("QA Automation Engineer");

        driver.findElement(By.id("radio-button-2")).click();

        driver.findElement(By.id("checkbox-1")).click();


        WebElement yearsOfExperienceDropdown = driver.findElement(By.id("select-menu"));
        yearsOfExperienceDropdown.click();

        WebDriverWait waitForList = new WebDriverWait(driver, 10);
        waitForList.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("option[value='1']"))).click();

        driver.findElement(By.id("datepicker")).sendKeys("03/03/2020");
        driver.findElement(By.id("datepicker")).sendKeys(Keys.RETURN);

        driver.findElement(By.cssSelector(".btn.btn-lg.btn-primary")).click();

        driver.quit();
    }
}
