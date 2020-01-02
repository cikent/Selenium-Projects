import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;

public class Radiobuttons {
    public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "C:\\Users\\Inciter\\Code\\Selenium Resources\\Selenium Drivers\\chromedriver.exe");

        WebDriver driver = new ChromeDriver();

        driver.get("https://formy-project.herokuapp.com/checkbox");

        WebElement checkbox1 = driver.findElement(By.id("checkbox-1"));
        checkbox1.click();

        WebElement checkbox2 = driver.findElement(By.id("checkbox-2"));
        checkbox2.click();

        WebElement checkbox3 = driver.findElement(By.id("checkbox-3"));
        checkbox3.click();

        driver.quit();
    }
}
