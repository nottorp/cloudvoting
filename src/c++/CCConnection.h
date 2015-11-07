namespace cloudclient {
	class CCConnection {

	private:
		int socket;

	public:
		void connect();

		void recv();

		void send();

		void check();
	};
}
