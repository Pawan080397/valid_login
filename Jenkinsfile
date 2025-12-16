post {
    always {
        echo "Publishing HTML Report"
        publishHTML(target: [
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: '.',
            reportFiles: 'report.html',
            reportName: 'Selenium Test Report'
        ])
    }

    success {
        echo "✅ Selenium tests passed"
    }

    failure {
        echo "❌ Selenium tests failed"
    }
}
