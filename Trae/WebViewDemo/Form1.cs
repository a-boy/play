namespace WebViewDemo;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
        InitializeWebView();
    }

    private async void InitializeWebView()
    {
        await webView.EnsureCoreWebView2Async(null);
        webView.CoreWebView2.Navigate(addressBar.Text);

        btnGo.Click += (s, e) => webView.CoreWebView2.Navigate(addressBar.Text);
        btnBack.Click += (s, e) => { if (webView.CanGoBack) webView.GoBack(); };
        btnForward.Click += (s, e) => { if (webView.CanGoForward) webView.GoForward(); };
        btnRefresh.Click += (s, e) => webView.Reload();

        webView.NavigationCompleted += (s, e) => addressBar.Text = webView.Source.ToString();

        addressBar.KeyPress += (s, e) =>
        {
            if (e.KeyChar == (char)Keys.Enter)
            {
                webView.CoreWebView2.Navigate(addressBar.Text);
                e.Handled = true;
            }
        };
    }
}
