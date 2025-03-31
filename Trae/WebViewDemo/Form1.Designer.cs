namespace WebViewDemo;

partial class Form1
{
    private System.ComponentModel.IContainer components = null;
    private Microsoft.Web.WebView2.WinForms.WebView2 webView;
    private TextBox addressBar;
    private Button btnGo;
    private Button btnBack;
    private Button btnForward;
    private Button btnRefresh;

    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
        webView = new Microsoft.Web.WebView2.WinForms.WebView2();
        addressBar = new TextBox();
        btnGo = new Button();
        btnBack = new Button();
        btnForward = new Button();
        btnRefresh = new Button();

        SuspendLayout();

        // addressBar
        addressBar.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
        addressBar.Location = new Point(90, 12);
        addressBar.Name = "addressBar";
        addressBar.Size = new Size(580, 23);
        addressBar.Text = "https://www.bing.com";

        // btnGo
        btnGo.Anchor = AnchorStyles.Top | AnchorStyles.Right;
        btnGo.Location = new Point(676, 12);
        btnGo.Name = "btnGo";
        btnGo.Size = new Size(75, 23);
        btnGo.Text = "转到";
        btnGo.UseVisualStyleBackColor = true;

        // btnBack
        btnBack.Location = new Point(12, 12);
        btnBack.Name = "btnBack";
        btnBack.Size = new Size(23, 23);
        btnBack.Text = "←";
        btnBack.UseVisualStyleBackColor = true;

        // btnForward
        btnForward.Location = new Point(35, 12);
        btnForward.Name = "btnForward";
        btnForward.Size = new Size(23, 23);
        btnForward.Text = "→";
        btnForward.UseVisualStyleBackColor = true;

        // btnRefresh
        btnRefresh.Location = new Point(58, 12);
        btnRefresh.Name = "btnRefresh";
        btnRefresh.Size = new Size(23, 23);
        btnRefresh.Text = "⟳";
        btnRefresh.UseVisualStyleBackColor = true;

        // webView
        webView.AllowExternalDrop = true;
        webView.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        webView.CreationProperties = null;
        webView.DefaultBackgroundColor = Color.White;
        webView.Location = new Point(12, 41);
        webView.Name = "webView";
        webView.Size = new Size(760, 408);
        webView.TabIndex = 0;
        webView.ZoomFactor = 1D;

        // Form1
        AutoScaleDimensions = new SizeF(7F, 17F);
        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(784, 461);
        Controls.Add(webView);
        Controls.Add(addressBar);
        Controls.Add(btnGo);
        Controls.Add(btnBack);
        Controls.Add(btnForward);
        Controls.Add(btnRefresh);
        Name = "Form1";
        Text = "WebView2演示";
        ResumeLayout(false);
        PerformLayout();
    }
}
