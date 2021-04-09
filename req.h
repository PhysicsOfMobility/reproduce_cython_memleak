#include <utility>

using namespace std;
namespace cstuff {
    template<typename Loc>
    class Request {
    public:
        int request_id;
        double creation_timestamp;

        Request() = default;
        Request(
            int request_id,
            double creation_timestamp
            ) :
            request_id{request_id},
            creation_timestamp{creation_timestamp} {};
        ~Request()=default;
    };
}

