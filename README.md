# GitHub Daily Contributions Bot 🤖

An automated script that makes 1-10 random contributions to your GitHub profile every day.

## 🎯 What It Does

- Runs automatically every day via GitHub Actions
- Makes a random number of contributions (1-10) each day
- Keeps your contribution graph active without manual effort
- No meaningful code changes - just appends timestamps to a file

## 🚀 Setup Instructions

### 1. Create a New Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new **public** repository (private repos don't show contributions on your profile)
3. Name it whatever you like (e.g., `daily-contributions`, `activity-bot`)
4. **Do NOT** initialize with README, .gitignore, or license

### 2. Push This Code

```bash
cd github-daily-contributions
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values.

### 3. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on the **Actions** tab
3. If prompted, click **"I understand my workflows, go ahead and enable them"**
4. The workflow should now be enabled and will run daily at 7:30 AM UTC

### 4. Test It (Optional)

You can manually trigger the workflow to test it:

1. Go to **Actions** tab in your repository
2. Click on **"Daily Contributions"** workflow
3. Click **"Run workflow"** button
4. Select the branch and click **"Run workflow"**

## 📊 How It Works

1. **GitHub Actions** runs the workflow daily based on the cron schedule
2. The Python script generates a random number between 1-10
3. For each contribution, it appends a timestamp to `contributions.txt`
4. Changes are committed and pushed back to the repository
5. Each commit counts as a contribution on your GitHub profile

## ⚙️ Customization

### Change the Time

Edit `.github/workflows/daily-contribution.yml` and modify the cron expression:

```yaml
schedule:
  - cron: '30 7 * * *'  # Currently 7:30 AM UTC
```

[Cron expression help](https://crontab.guru/)

### Change Contribution Range

Edit `contribute.py` and modify line 15:

```python
num_contributions = random.randint(1, 10)  # Change min/max values
```

## 📝 Files

- `contribute.py` - Python script that makes random contributions
- `.github/workflows/daily-contribution.yml` - GitHub Actions workflow
- `contributions.txt` - File that gets updated (created automatically)

## ⚠️ Note

This repository is for educational purposes. Keep in mind that:
- Commits should ideally represent real work
- This creates "artificial" activity on your profile
- Use responsibly and transparently

## 📜 License

Free to use however you want!
