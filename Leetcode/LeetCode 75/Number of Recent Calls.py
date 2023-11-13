class RecentCounter {
public:
    RecentCounter() {}
    
    int ping(int t) {
        while (!q.empty()) {
        	if (q.front() + 3000 >= t) break;
        	q.pop();
        }
        q.push(t);
        return q.size();
    }

private:
	queue<int> q;
};
